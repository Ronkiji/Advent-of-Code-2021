
input = [(line.rstrip('\n')) for line in open("inputs/day03.txt")]

# part 1

first = ""
second = ""

for i in range(len(input[0])):
  one = 0
  zero = 0
  for line in input:
    if line[i] == "1":
      one += 1
    else:
      zero += 1
  
  if one > zero:
    first += "1"
    second += "0"
  else:
    first += "0"
    second += "1"

print(int(first, 2) * int(second, 2))

# part 2

oxy = input[0:].copy()
length = len(input[0])

while(len(oxy) != 1):
  for i in range(length):
    if len(oxy) == 1:
      break
    ones = []
    zeros = []

    one = 0
    zero = 0
    for k in range(len(oxy)):
      if oxy[k][i] == "1":
        one += 1
        ones.append(k)
      else:
        zero += 1
        zeros.append(k)
    if one > zero:
      for m in range(len(zeros)):
        oxy.pop(zeros[m]-m)
    elif zero > one:
      for m in range(len(ones)):
        oxy.pop(ones[m]-m)
    else:
      for m in range(len(zeros)):
        oxy.pop(zeros[m]-m)


oxy2 = input[0:].copy()

length = len(input[0])

while(len(oxy2) != 1):

  for i in range(length):
    if len(oxy2) == 1:
      break
    ones = []
    zeros = []

    one = 0
    zero = 0
    for k in range(len(oxy2)):
      if oxy2[k][i] == "1":
        one += 1
        ones.append(k)
      else:
        zero += 1
        zeros.append(k)

    if one > zero:
      for m in range(len(ones)):
        oxy2.pop(ones[m]-m)
    elif zero > one:
      for m in range(len(zeros)):
        oxy2.pop(zeros[m]-m)
    else:
      for m in range(len(ones)):
        oxy2.pop(ones[m]-m)

print(int(oxy[0], 2) * int(oxy2[0], 2))





