input = [int(line.rstrip('\n')) for line in open("inputs/day01.txt")]

# part 1
count = 0
for i in range(len(input)-1):
  if input[i+1] > input[i]:
    count += 1
  
print(count)

# part 2
count = 0
for i in range(len(input)-3):
  if input[i+3] > input[i]:
    count += 1
  
print(count)