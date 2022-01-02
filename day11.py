content = [(line.rstrip('\n')) for line in open("inputs/day11.txt")]

input = [[int(x) for x in line] for line in content]

# part 1

adj = [(0,1),(0,-1),(1, 0),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1)]

flashes = 0

def fill(row, col):
  if input[row][col] == 0:
    return 0
  elif input[row][col] > 9:
    input[row][col] = 0
    return 1 + sum(fill(row + x, col + y) for x, y in adj if 0 <= row + x < len(input) and 0 <= col + y < len(input[0]))
  else:
    input[row][col] += 1
    return fill(row, col) if input[row][col] > 9 else 0

steps = 1

while(True):

  input = [[num + 1 for num in line] for line in input]

  for y in range(len(input)):
    for x in range(len(input[y])):
      if input[y][x] > 9:
        flashes += fill(y, x)
  
  if steps == 100:
    print(flashes)
  
  # part 2

  if sum(x.count(0) for x in input) == len(input) * len(input[0]):
    print("All flashes at step " + str(steps))
    break

  steps += 1