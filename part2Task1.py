"""
BFS
"""


def bfs(map, office):
    adjacencyList = helpAdjList(map)

    visitstatus = {}
    mypaths = []
    myqueue = []
    myqueue.append(office)

    visitstatus[office] = True

    for i in adjacencyList:
        key = i[0]
        visitstatus.append({key: False})

    print(visitstatus)

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
    adjacencyList = helpAdjList(map)

    visitstatus = {}

    for nextnode in map[office]:
        if visitstatus == False:
            visitstatus.add(office)
            return dfs(map, nextnode)


"""
Dijkstra's
"""


def dijkstra(map, office):
	
    return


def helpAdjList(input):
    adjacencyList = defaultdict(list)
    # build an adjacency dictionary
    for i in input:

        nodeU = i[0]
        nodeV = i[1]
        weight = i[2]

        try:
            adjacencyList[nodeU].append(nodeV)

        except KeyError:
            print("adding new location to Adjacency List")
            adjacencyList.append({nodeU: nodeV})
            print("updated adjacencyList")

    return adjacencyList
