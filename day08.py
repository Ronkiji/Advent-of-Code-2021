content = [(line.rstrip('\n')) for line in open("inputs/day08.txt")]



# [x, y, z]
# input = [int(y) for y in content[0].split(",")]

# [[a, b], [c, d]]
# input = [[key, int(val)] for key, val in (line.split(" ") for line in in)]

# [[a, b, c, d], [a, b, c, d], [a, b, c, d]]

# input = [[int(x) for x in line] for line in content]

# part 1

input = []
output = []
lines = []
for line in content:

  l, r = line.split(" | ")
  lines.append(l)
  input.append(l.split(" "))
  output.append(r.split(" "))

count = 0

for y in output:
  for x in y:
    if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7:
      count += 1

print(count)

# part 2


default = {0:'123456', 1:'23', 2:'12754', 3:'12734', 4:'6723', 5:'16734', 6:'167543', 7:'123', 8:'1234567', 9:'126734'}

nums = []

letters = ['a','b','c','d','e','f','g']
for i in range(len(input)):
  order = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
  numbers = []
  eights = []
  sevens = []
  for x in letters:
    count = lines[i].count(x)
    if count == 6:
      order[6] = x
    elif count == 4:
      order[5] = x
    elif count == 9:
      order[3] = x 
    elif count == 8:
      eights.append(x)
    else:
      sevens.append(x)
  
  for x in eights:
    if x in sorted(input[i], key=len)[0]:
      order[2] = x
    else:
      order[1] = x

  for x in sevens:    
    if x in sorted(input[i], key=len)[2]:
      order[7] = x
    else:
      order[4] = x
  
  for x in range(10):
    numstring = default[x]
    string = ''
    for digit in numstring:
      string += order[int(digit)]
    numbers.append(''.join(string))

  num = ''
  for sets in output[i]:
    for index in range(10):
      if sorted(sets) == sorted(numbers[index]): 
        num += str(index)
        break
  nums.append(int(num))

print(sum(nums))