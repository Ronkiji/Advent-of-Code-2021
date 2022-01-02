input = [(line.rstrip('\n')) for line in open("inputs/day05.txt")]
sets = [y.split(" -> ") for y in input]

def convert(sets):
  if type(sets) == list:
    return str(sets[0]) + "," + str(sets[1])
  else:
    return [int(num) for num in sets.split(",")]

track = {}

def append(value):
  # print(value)
  if value in track:
    track[value] += 1
  else:
    track[value] = 1


for s in sets:
  first = convert(s[0])
  sec = convert(s[1])

  fcopy = first[:]

  if first[0] == sec[0]:
    append(convert(first))
    if first[1] < sec[1]:
      while first[1] < sec[1]:
        first[1] += 1
        append(convert(first))
    elif first[1] > sec[1]:
      while first[1] > sec[1]:
        first[1] -= 1
        append(convert(first))
  elif first[1] == sec[1]:
    append(convert(first))
    if first[0] < sec[0]:
      while first[0] < sec[0]:
        first[0] += 1
        append(convert(first))
    if first[0] > sec[0]:
      while first[0] > sec[0]:
        first[0] -= 1
        append(convert(first))

  # part 2
  elif abs(sec[1]-first[1]) == abs(sec[0]-first[0]):
    append(convert(first))
    while((first[0] != sec[0]) or (first[1] != sec[1])):
      if first[0] < sec[0]:
        first[0] += 1
      elif first[0] > sec[0]:
        first[0] -= 1
      if first[1] < sec[1]:
        first[1] += 1
      elif first[1] > sec[1]:
        first[1] -= 1
      
      append(convert(first))


print(len(track.values()) - sum(value == 1 for value in track.values()))