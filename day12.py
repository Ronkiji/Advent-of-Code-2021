content = [(line.rstrip('\n')) for line in open("inputs/day12.txt")]

input = [[key, val] for key, val in (line.split("-") for line in content)]
print(input)

start = []
end = []
paths = {}

def search(u):
	global res
	if u == 'end':
		res += 1
	
	visited[u] = True
	for v in graph[u]:
		if not visited[v] or v.isupper():
			search(v)
	
	visited[u] = False

graph = {}

for set in input:
  u = set[0]
  v = set[1]
  if u not in graph:
    graph[u] = []
  if v not in graph:
    graph[v] = []
  graph[u].append(v)
  graph[v].append(u)

visited = {i: False for i in graph.keys()}
visited['start'] = True
res = 0
search('start')

print(res)

def search2(u, b):
	global res
	if u == 'end':
		res += 1
		return
	
	visited[u] += 1

	for v in graph[u]:
		if v.isupper():
			search2(v, b)
		elif visited[v] == 0:
			search2(v, b)
		elif visited[v] == 1 and not b:
			search2(v, True)
	
	visited[u] -= 1

graph = {}

for set in input:
  u = set[0]
  v = set[1]
  if u not in graph:
    graph[u] = []
  if v not in graph:
    graph[v] = []
  graph[u].append(v)
  graph[v].append(u)

visited = {i: 0 for i in graph.keys()}
visited['start'] = 2
res = 0
search2('start', False)

print(res)