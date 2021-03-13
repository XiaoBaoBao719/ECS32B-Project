"""
BFS
"""


def bfs(map, office):

	adjacencyList = defaultdict(list)
	#build an adjacency dictionary 
	for i in map:

		nodeU = i[0]
		nodeV = i[1]
		weight = i[2]

		try:
			adjacencyList[nodeU].append(nodeV)

		except KeyError:
			print("adding new location to Adjacency List")
			adjacencyList.append({nodeU : nodeV})
			print("updated adjacencyList")

	visitstatus = [False] * (max(map) + 1)
	mypaths = []
	myqueue = []
	myqueue.append(office)

	visitstatus[office] = True

	while myqueue:
		office = myqueue.pop(0)

		for nextnode in map[office]:
			if visitstatus[nextnode] == False:
				myqueue.append(nextnode)
				visitstatus[nextnode] = True

	return mypaths


"""
DFS
"""


def dfs(map, office):
    visitstatus = [False] * (max(map) + 1)

    if visitstatus == False:
        visitstatus.add(office)
        for nextnode in map[office]:
            return dfs(map, nextnode)

"""
Dijkstra's
"""


def dijkstra(map, office):
    return
