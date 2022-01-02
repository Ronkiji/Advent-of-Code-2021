content = [(line.rstrip('\n')) for line in open("inputs/day15.txt")]

input = [[int(x) for x in line] for line in content]

xmax = len(input[0])
ymax = len(input)

def part1():

  score_pos = [(0, 0, 0)]

  costs = {}

  while True:
    cost, x, y = score_pos[0]
    
    if x == xmax-1 and y == ymax-1: 
      print(cost)
      break

    score_pos = score_pos[1:]

    for xx, yy in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
      
      if xx in range(xmax) and yy in range(ymax):

        score = cost + input[xx][yy]
        
        if (xx, yy) in costs and costs[(xx, yy)] <= score:
          continue
        
        costs[(xx, yy)] = score
        score_pos.append((score, xx, yy))
        
    score_pos = sorted(score_pos)
    print(score_pos)

# part1()

def part2():
  global input, xmax, ymax

  new = [[None for x in range(xmax*5)] for y in range(ymax * 5)]

  for x in range(len(input)):
    for y in range(len(input[0])):
      new[x][y] = input[x][y]
  
  for index in range(len(input)):
    for loop in range(4):
      nextlist = [num + 1 for num in input[index]]
      for y in range(len(nextlist)):
        if nextlist[y] == 10:
          nextlist[y] = 1
        new[index + (loop + 1) * len(input)][y] = nextlist[y]

  for y in range(len(new)):
    for x in range(len(input[0])):
      currentx = new[x][y]
      for loop in range(4):
        currentx += 1
        if currentx == 10:
          currentx = 1
        new[y][x + (loop + 1) * len(input[0])] = currentx
  
  xmax = len(new[0])
  ymax = len(new) 

  score_pos = [(0, 0, 0)]

  costs = {}

  while True:
    cost, x, y = score_pos[0]
    
    if x == xmax-1 and y == ymax-1: 
      print(cost)
      break

    score_pos = score_pos[1:]

    for xx, yy in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
      
      if xx in range(xmax) and yy in range(ymax):
        score = cost + new[xx][yy]
        if (xx,yy) in costs and costs[(xx, yy)] <= score:
          continue
        costs[(xx,yy)] = score
        score_pos.append((score, xx, yy))
        
    score_pos = sorted(score_pos) 


part1()
part2()