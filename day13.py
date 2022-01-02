
content = [(line.rstrip('\n')) for line in open("inputs/day13.txt")]

graph = {}
dots = []
folds = []
stilldots = True

for line in content:
  if line == '':
    stilldots = False
  elif stilldots == True:
    x, y = line.split(',')
    dots.append([int(x), int(y)])
  elif stilldots == False:
    if 'x' in line:
      random, num = line.split('=')
      folds.append(['x', int(num)])
    else:
      random, num = line.split('=')
      folds.append(['y', int(num)])

xmax = max(dot[0] for dot in dots) + 1
ymax = max(dot[1] for dot in dots) + 1

for x in range(xmax):
  for y in range(ymax):
    graph[x,y] = '-'

print(xmax)
print(ymax)

for dot in dots:
  graph[dot[0], dot[1]] = '#'

for fold in folds:
  print(fold)

  if fold[0] == 'y':
    row = fold[1]
    for col in range(xmax):
      del graph[col, row]
      for rowx in range(row + 1, ymax):
        if graph[col, rowx] == '#':

          graph[col, row - (rowx - row)] = '#'

        del graph[col, rowx]

    ymax = ymax//2

  if fold[0] == 'x':
    col = fold[1]
    for row in range(ymax):
      del graph[col, row]
      for colx in range(col + 1, xmax):
        if graph[colx, row] == '#':
          graph[col - (colx - col), row] = '#'
          
        del graph[colx, row]
    
    xmax = xmax//2


print(sum(value == '#' for value in graph.values()))

print(graph)

for y in range(ymax):
  string = ''
  for x in range(xmax):
    string += graph[x, y]
  print(string)
