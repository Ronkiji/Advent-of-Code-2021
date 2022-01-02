content = [(line.rstrip('\n')) for line in open("inputs/day16.txt")]

hexa = content[0]

alpha = {'0':'0000', '1':'0001', '2': '0010', '3': '0011', '4':'0100', '5': '0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A': '1010', 'B': '1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

binary = ''

for letter in hexa:
  binary += alpha[letter]

versions = []

total = 0


def parse(binary):

  global versions

  versions.append(int(binary[:3], 2))

  ID = int(binary[3:6], 2)

  binary = binary[6:]

  if ID == 4:

    binaryline = ''

    while True:

      leading = binary[0]
      binaryline += binary[1:5]

      binary = binary[5:]

      if leading == '0':
        break

    return (binary, int(binaryline, 2))

  else:

    leading, binary = binary[0], binary[1:]

    nums = []

    if leading == '0':
      
      next15, binary = binary[:15], binary[15:]

      lenpackets = int(next15, 2)
      packets = binary[:lenpackets]

      while len(packets) != 0:
        packets, num = parse(packets)
        nums.append(num)

      binary = binary[lenpackets:]
      
    else:

      next11, binary = binary[:11], binary[11:]
      countpackets = int(next11, 2)

      for i in range(countpackets):
        binary, num = parse(binary)
        nums.append(num)
    
    if ID == 0:
      return (binary, sum(nums))
    elif ID == 1:
      product = 1
      for i in nums:
        product *= i
      return (binary, product)
    elif ID == 2:
      return (binary, min(nums))
    elif ID == 3:
      return (binary, max(nums))
    elif ID == 5:
      return (binary, 1 if nums[0] > nums[1] else 0)
    elif ID == 6:
      return (binary, 1 if nums[0] < nums[1] else 0)
    elif ID == 7:
      return (binary, 1 if nums[0] == nums[1] else 0)
  
results = parse(binary)[1]

print("Part1")
print(sum(versions))
print()
print("Part2")
print(results)