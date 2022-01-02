content = [(line.rstrip('\n')) for line in open("inputs/day09.txt")]

nums = []
low_val = []

num_rows = len(input)
num_cols = len(input[0])

N = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for y in range(len(input)):
  for x in range(len(input[y])):
    check = True
    current = input[y][x]
    for row, col in N:
      newx = x + row
      newy = y + col
      if 0 <= x + row < num_rows and 0 <= y + col < num_cols:
        if current >= input[newy][newx]: check = False
    if check == True:
      nums.append(current)
      low_val.append([x, y])

print(sum(nums) + len(nums))

def fill(row, col):
  if input[row][col] == 9:
    return 0
  input[row][col] = 9
  return 1 + sum(fill(row + x, col + y) for x, y in N if 0 <= row + x < num_rows and 0 <= col + y < num_cols)

basinsizes = []
for low in low_val:
  basinsizes.append(fill(low[0],  low[1]))

basinsizes = sorted(basinsizes, reverse = True)
print(basinsizes[0] * basinsizes[1] * basinsizes[2])