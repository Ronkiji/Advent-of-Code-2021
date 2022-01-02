# [x, y, z]
# input = [int(y) for y in content[0].split(",")]

# [[a, b], [c, d]]
# input = [[key, int(val)] for key, val in (line.split(" ") for line in in)]

# [[a, b, c, d], [a, b, c, d], [a, b, c, d]]
# input = [[int(x) for x in line] for line in content]

content = [(line.rstrip('\n')) for line in open("inputs/day18.txt")]
