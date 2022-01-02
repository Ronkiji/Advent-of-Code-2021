
input = [(line.rstrip('\n')) for line in open("inputs/day04.txt")]
nums = [int(y) for y in input[0].split(",")]

# part 1

def check(b):
  for x in b:
    # print(x)
    count1 = 0
    count2 = 0
    for y in x:
      for z in y:
        if z[1] == 1:
          count1 += 1 
          # print(count1)
      if count1 == 5:
        return x
      count1 = 0
    for i in range(5):
      count2 = 0
      for j in range(5):
        if x[j][i][1] == 1:
          count2 += 1
      if count2 == 5:
        return x
      count2 = 0



bingos = []
# print(bingos)
index = 0
temp = []
temp2 = []
for i in input[2:]:
  temp = []
  if index == 5:
    index = 0
    bingos.append(temp2)
    temp2 = []
  else:
    i = i.split(" ")
    while "" in i:
      i.remove("")
    # print(i)
    for x in i:
      temp.append([int(x), 0])
    temp2.append(temp)
    index += 1



loop = 0
winner = [0]
for i in nums:
  
  for x in bingos:
    for y in x:
      for z in y:
      # print(y)
        if z[0] == i:
          z[1] = 1
  if loop > 5:
    result = check(bingos)
    if result != None:
      print(i)
      print(result)
      break
  loop += 1

print((54 + 41 + 33 + 60 + 85 + 77 + 51 + 81 + 12 + 20 + 27 + 36 + 24 + 80 + 14 + 83 + 50 + 91) * 49)
print()
print()
print()


# part 2


def check(b):
  for x in b:
    # print(x)
    count1 = 0
    count2 = 0
    for y in x:
      for z in y:
        if z[1] == 1:
          count1 += 1 
          # print(count1)
      if count1 == 5:
        return x
      count1 = 0
    for i in range(5):
      count2 = 0
      for j in range(5):
        if x[j][i][1] == 1:
          count2 += 1
      if count2 == 5:
        return x
      count2 = 0



bingos = []
# print(bingos)
index = 0
temp = []
temp2 = []
for i in input[2:]:
  temp = []
  if index == 5:
    index = 0
    bingos.append(temp2)
    temp2 = []
  else:
    i = i.split(" ")
    while "" in i:
      i.remove("")
    # print(i)
    for x in i:
      temp.append([int(x), 0])
    temp2.append(temp)
    index += 1



loop = 0
winner = [0]
onlyone = False
for i in nums:
  
  for x in bingos:
    for y in x:
      for z in y:
      # print(y)
        if z[0] == i:
          z[1] = 1
  if loop > 5:
    if onlyone == False:
      while check(bingos) != None:
        bingos.remove(check(bingos))
        if len(bingos) == 1:
          onlyone = True
          break
      if len(bingos) == 1:
        onlyone = True
    else:
      if check(bingos) != None:
        print(check(bingos))
        print(i)
        break
        break
        break
        

  loop += 1


print((67 + 77 + 37 + 59 + 81) * 8)