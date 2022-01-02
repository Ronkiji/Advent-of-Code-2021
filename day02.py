input = [(line.rstrip('\n')) for line in open("inputs/day02.txt")]
inp = [[key, int(val)] for key, val in (line.split(" ") for line in input)]

# part 1
pos = [0, 0]

for i in inp:
  if i[0] == "forward":
    pos[0] += i[1]
  elif i[0] == "down":
    pos[1] += i[1]
  elif i[0] == "up":
    pos[1] -= i[1]
  
print(pos[0] * pos[1])

# part 2

pos = [0, 0, 0]

for i in inp:
  if i[0] == "forward":
    pos[0] += i[1]
    pos[1] = pos[1] + (pos[2] * i[1])
  elif i[0] == "down":
    pos[2] += i[1]
  elif i[0] == "up":
    pos[2] -= i[1]
  
print(pos[0] * pos[1])