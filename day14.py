
h = (0, 1)
print(h[0])

content = [(line.rstrip('\n')) for line in open("inputs/day14.txt")]

def part1():
  global content
  original = content[0]
  print(original)

  insertions = {}

  for line in content[2:]:
    x, y = line.split(' -> ')
    l1, l2 = x[0], x[1]
    charas = (l1, l2)
    insertions[charas] = y

  for i in range(10):
    newline = original[0]
    for x in range(1, len(original)):
      charas = (original[x-1], original[x])
      if charas in insertions.keys():
        newline += insertions[charas] + original[x]
    
    original = newline[:]
    # print(original)


  print(original)
  print(len(original))
  print(max(original, key=original.count))
  print(min(original, key=original.count))
  print(original.count('H') - original.count('C'))


def part2():

  global content
  original = content[0]
  print(original)

  insertions = {}

  for line in content[2:]:
    x, y = line.split(' -> ')
    l1, l2 = x[0], x[1]
    charas = (l1, l2)
    insertions[charas] = y

  characters = {}
  for x in original:
    if x in characters.keys():
      characters[x] += 1
    else:
      characters[x] = 1
  print(characters)
  
  initial = {}

  for x in range(1, len(original)):
    if (original[x-1], original[x]) in initial.keys():
      initial[(original[x-1], original[x])] += 1
    else:
      initial[(original[x-1], original[x])] = 1

  print(initial)
  print()

  for i in range(40):
    second = initial.copy()
    for sets in initial.keys():
      left, right = sets[0], sets[1]
      middle = insertions[(left, right)]
      v = initial[sets]
    
      
      if (left, middle) in second.keys():
        second[(left, middle)] += v
      else:
        second[(left, middle)] = v
      
      if (middle, right) in second.keys():
        second[(middle, right)] += v
      else:
        second[(middle, right)] = v
      
      if middle in characters.keys():
        characters[middle] += v
      else:
        characters[middle] = v
      second[(left, right)] -= v
    
    initial = second.copy()
      
    print(initial)
    print(characters)
    print()
  
  print(max(characters.values()) - min(characters.values()))


part2()

# n: 2
# c: 1
# b: 1

# NNCB

# {
#   (nn): 1
#   (nc): 1
#   (cb): 1
# }

# adjacents = {
#   (nn): 0 --> ncn
#   (nc): 1
#   (cb): 1
#   (cn): 1
#   (nb): 1
#   (bc): 1
# }

# Template:     NNCB
# After step 1: NCNBCHB