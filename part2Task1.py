import heapq as heap
from collections import defaultdict
import math
from array import *


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


"""
BFS
"""


def bfs(map, office):

    #A DICTIONARY OF THE PATHS FROM SOURCE TO EACH UNIQUE DESTINATION
    mypaths = {}

    # for destination in getLocations(map):
    for destination in getLocations(map):
        # reset visited list
        # visited = []
        # reset queue to start with the office
        # visited.append(office)
        # myqueue.append(office)
        validPath = bfsHelper(map, office, destination)
        # print(validPath)
        # print(allPaths(map, office, destination))
        # UPDATE PATH DICTIONARY WITH NEW KEY:PATH PAIRING
        mypaths.update({destination: validPath})

    return mypaths

def bfsHelper(map, start, destination):

    myqueue = []
    myqueue.append([start])
    visited = []

    while myqueue:
            currentPath = myqueue.pop(0)
            visited.append(currentPath[-1])
            #print(myqueue)
            lastItem = currentPath[-1]
            curIndex = getLocations(map).index(lastItem)
            adjIndices = [index for index, element in enumerate(getAdjacencyMap(map)[curIndex]) if element >= 0]

            if(lastItem == destination):
                return currentPath

            adjVertices = []
            for i in adjIndices:
                adjVertices.append(getLocations(map)[i])

            for adjacent in adjVertices:
                if(adjacent not in visited):
                    newPath = list(currentPath)
                    #print(newPath)

                    newPath.append(adjacent)
                    myqueue.append(newPath)
"""
DFS
"""


def dfs(map, office):
    matrixMap = getAdjacencyMap(map)
    locations = getLocations(map)

    output = {}

    for destination in locations:
        print("CURRENT DESTINATION: ", destination)

        newpathidea = allPaths(map, office, destination)
        print(newpathidea)
        path = []
        stack = []
        visited = [office]

        path = dfsHelper(map, office, destination)
        # print("exiting")
        # print(stack)
        output.update({destination: path})

    return output


def dfsHelper(map, start, destination):
    # parentMap = []
    path = []
    visited = []
    stack = []
    # visited.append(start)
    stack.append([start])

    visitTracker = []
    # print("CURRENT NODE:", start)

    # get adjacent nodes
    curIndex = getLocations(map).index(start)
    indices = [index for index, element in enumerate(getAdjacencyMap(map)[curIndex]) if element >= 0]
    adjVertices = []
    for i in indices:
        adjVertices.append(getLocations(map)[i])

    while stack:

        # print(stack)
        currentPath = stack.pop()

        print(currentPath)
        # path.append(currentPath)

        if (currentPath[-1] in visited):
            # path.pop()
            continue
        if (currentPath[-1] == destination):
            # print(stack)
            # x = 10 / 0
            print("Path found!")
            return currentPath

        visited.append(currentPath[-1])

        curIndex = getLocations(map).index(currentPath[-1])
        indices = [index for index, element in enumerate(getAdjacencyMap(map)[curIndex]) if element >= 0]
        adjVertices = []
        for i in indices:
            adjVertices.append(getLocations(map)[i])

        for j in adjVertices:
            if j not in visited:
                newPath = list(currentPath)
                newPath.append(j)
                stack.append(newPath)


"""
Dijkstra's
"""


def dijkstra(map, office):

    # Creating andf using adjaceny Matrix
    matrix = getAdjacencyMap(map)
    # Creating locations vector containing strings in alpabetical order
    locations = getLocations(map)

    # Setting all distances equal to infinite
    distances = [math.inf for i in range(len(matrix))]
    print(distances)
    # Creating list to check if each city is visited
    visited = [False for j in range(len(matrix))]
    print(visited)

    # Setting office distance equal to zero
    officeIndex = getLocations(map).index('UPS')
    distances[officeIndex] = 0
    row = len(matrix)
    parent = [-1] * row

    route = []
    # while the visited status is true
    while True:  # "while true"

        # Finding node that hasnt been visited yet
        shortDist = math.inf  # shortest distance
        shortIndex = -1  # shortest index, will check if previous node has shorter distance than current node

        for k in range(len(matrix)):
            # print(distances)
            if distances[k] < shortDist and visited[k] is False:
                shortDist = distances[k]
                shortIndex = k
                # print(shortDist)
                # print(shortIndex)

        print(shortIndex)
        # Checking to see if any nodes were not yet visited
        if shortIndex == -1:
            print("It was negative 1")
            break
        else:
            for l in range(len(matrix[shortIndex])):
                # Relazation ahhhhh
                if matrix[shortIndex][l] != 0 and distances[l] > distances[shortIndex] + matrix[shortIndex][l]:
                    # Make this the now shortest path
                    distances[l] = distances[shortIndex] + matrix[shortIndex][l]
                    parent[l] = shortIndex
            visited[shortIndex] = True

    # print("Visited nodes: " + str(visited))
    print("Currently lowest distances: " + str(distances))
    print(parent)
    finalpaths = []
    templist = []

    for i in range(len(matrix)):
        if i != office and distances[i] != math.inf:
            get_route(parent, i, route)
            print(f"Path ({office} —> {i}): Minimum cost = {distances[i]}, Route = {route}")
            # print(route)
            for q in range(len(route)):
                templist.append(locations[route[q]])
            finalpaths.append(list(templist))
            route.clear()
            templist.clear()
    print(finalpaths)
    finalDict = dict(zip(getLocations(map), finalpaths))

    return finalDict

# takes list of edges and returns a 2D list array
def getAdjacencyMap(edges):
    nodeMap = [[], []]
    # build an adjacency matrix
    locations = getLocations(edges)
    numLocations = len(locations)
    # print(sorted(locations))

    # create 3D matrix
    nodeMap = [[-1] * numLocations for i in range(numLocations)]
    #print(nodeMap)
    for u, v, weight in edges:
        #    print(u)
        #    print(v)
        #    print(weight)
        index1 = locations.index(u)
        index2 = locations.index(v)

        nodeMap[index1][index2] = weight
        nodeMap[index2][index1] = weight
    print(locations)
    #FOR CHECKING MATRIX
    # for i in range(len(nodeMap)):
    #     print(nodeMap[i])
    #     print("\n")


    return nodeMap


# returns a sorted list of the locations
def getLocations(edges):
    uniqueLocations = {edges[0][0]}

    for i in edges:

        nodeU = i[0]
        nodeV = i[1]
        weight = i[2]

        if (nodeU not in uniqueLocations):
            uniqueLocations.add(nodeU)
        if (nodeV not in uniqueLocations):
            uniqueLocations.add(nodeV)

    # print("UNIQUE LOCATIONS:")
    # print(uniqueLocations)

    return sorted(uniqueLocations)


def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)

def allPaths(edges, source, destination):
    adj_list = defaultdict(list)

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
    paths = [[source]]
    result = []

    while paths:
        path = paths.pop()
        u = path[-1]
        if u == destination:
            result.append(path)
        else:
            for v in adj_list[u]:
                paths.append(path + [v])
    return result

# TEST CASES
# m = [('UPS', 'Brecon', 28), ('UPS', 'Owl Ranch', 20), ('UPS', 'Sunfield', 17), ('Jacob City', 'Brecon', 25), ('Sunfield', 'Owl Ranch', 0)]
# val = dijkstra(m, 'UPS')
# print(val)

# val2 = dfs(m, 'UPS')
# print(val2)

# m = [('UPS', 'Brecon', 3), ('Jacob City', 'Owl Ranch', 3), ('Jacob City', 'Sunfield', 15), ('Sunfield', 'Brecon', 25)]
# val = bfs(m, 'UPS')
# print(val)

# m = [('UPS', 'Steuben', 15), ('Richmond Hill', 'Steuben', 20), ('Richmond Hill', 'Owl Ranch', 17), ('Richmond Hill', 'Diehlstadt', 27), ('Richmond Hill', 'Sunfield', 22), ('Richmond Hill', 'Holly Ridge', 13), ('Holly Ridge', 'Sunfield', 16), ('Holly Ridge', 'Hambleton', 17), ('Holly Ridge', 'Jacob City', 13), ('Holly Ridge', 'Owl Ranch', 0), ('Holly Ridge', 'Steuben', 17), ('Holly Ridge', 'Diehlstadt', 0), ('Jacob City', 'Owl Ranch', 13), ('Sunfield', 'Brecon', 24)]
# val = bfs(m, 'UPS')
# expected = {'UPS': ['UPS'], 'Steuben': ['UPS', 'Steuben'], 'Richmond Hill':['UPS', 'Steuben', 'Richmond Hill'], 'Owl Ranch': ['UPS', 'Steuben', 'Holly Ridge','Owl Ranch'], 'Diehlstadt': ['UPS', 'Steuben', 'Holly Ridge', 'Diehlstadt'], 'Sunfield': ['UPS', 'Steuben', 'Holly Ridge', 'Sunfield'], 'Holly Ridge': ['UPS', 'Steuben', 'Holly Ridge'], 'Hambleton': ['UPS', 'Steuben', 'Holly Ridge', 'Hambleton'], 'Jacob City': ['UPS', 'Steuben', 'Holly Ridge', 'Jacob City'], 'Brecon': ['UPS', 'Steuben', 'Holly Ridge', 'Sunfield', 'Brecon']}

#getAdjacencyMap(m)
# print(val)