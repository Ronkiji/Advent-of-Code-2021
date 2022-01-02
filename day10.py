content = [(line.rstrip('\n')) for line in open("inputs/day10.txt")]
input = [[char for char in line] for line in content]

close_to_open = {')': '(', ']': '[', '}': '{', '>': '<'}

points = {')': 3, ']': 57, '}': 1197, '>': 25137}

total = 0

for line in content:
  stack = []
  for char in list(line.strip()):
    if char in close_to_open.values():
      stack.append(char)
    elif not stack or stack.pop() != close_to_open[char]:
      total += points[char]
      break

print(total)

# part 2

scores = {'(': 1, '[': 2, '{': 3, '<': 4}

totals = []

for line in content:

  stack = []

  for char in list(line.strip()):

    if char in close_to_open.values():
      stack.append(char)
    elif not stack or stack.pop() != close_to_open[char]:
      stack = []
      break

  if stack:
    stack = stack[::-1]
    print(stack)
    score = 0
    for x in stack:
      score = score * 5 + scores[x]
    totals.append(score)
print(sorted(totals)[len(totals)//2])