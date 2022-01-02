input = [(line.rstrip('\n')) for line in open("inputs/day07.txt")]
nums = [int(y) for y in input[0].split(",")]


maxi = max(nums)

# part 1

distance = []

for i in range(len(nums)):
  total = 0
  for x in nums:
    total += abs(x-i)
  distance.append(total)
print(min(distance))

# part 2

distance = []

for i in range(len(nums)):
  total = 0
  for x in nums:
    total += sum(range(abs(x-i)+1))
  distance.append(total)
print(min(distance))