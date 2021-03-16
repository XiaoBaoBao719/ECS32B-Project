from collections import defaultdict
import math
from array import *

"""
BFS
"""


def bfs(map, office):
    # A DICTIONARY OF THE PATHS FROM SOURCE TO EACH UNIQUE DESTINATION
    mypaths = {}
    for destination in getLocations(map):
        # reset queue to start with the office
        validPath = bfsHelper(map, office, destination)
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
        # print(myqueue)
        lastItem = currentPath[-1]
        curIndex = getLocations(map).index(lastItem)
        adjIndices = [index for index, element in enumerate(getAdjacencyMap(map)[curIndex]) if element >= 0]

        if (lastItem == destination):
            return currentPath

        adjVertices = []
        for i in adjIndices:
            adjVertices.append(getLocations(map)[i])

        for adjacent in adjVertices:
            if (adjacent not in visited):
                newPath = list(currentPath)
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
        # print("CURRENT DESTINATION: ", destination)
        path = dfsHelper(map, office, destination)
        output.update({destination: path})

    return output


def dfsHelper(map, start, destination):
    visited = []
    stack = []
    stack.append([start])

    # print("CURRENT NODE:", start)
    # get adjacent nodes
    curIndex = getLocations(map).index(start)
    indices = [index for index, element in enumerate(getAdjacencyMap(map)[curIndex]) if element >= 0]
    adjVertices = []
    for i in indices:
        adjVertices.append(getLocations(map)[i])

    while stack:
        currentPath = stack.pop()
        # print(currentPath)

        if currentPath[-1] in visited:
            continue
        if currentPath[-1] == destination:
            # print("Path found!")
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
    matrix = getAdjacencyMap(map)
    locations = getLocations(map)

    row = len(matrix)
    col = len(matrix[0])

    distances = [math.inf] * row
    parent = [-1] * row

    officeIndex = getLocations(map).index('UPS')  # Setting office distance from itself equal to zero
    distances[officeIndex] = 0

    myqueue = []
    for i in range(row):
        myqueue.append(i)
    route = []
    while myqueue:
        shortDist = math.inf  # shortest distance
        shortIndex = -1  # shortest index, will check if previous node has shorter distance than current node

        for k in range(len(matrix)):
            if distances[k] < shortDist and k in myqueue:
                shortDist = distances[k]
                shortIndex = k

        myqueue.remove(shortIndex)

        for i in range(col):
            if matrix[shortIndex][i] >= 0 and i in myqueue:
                if distances[shortIndex] + matrix[shortIndex][i] < distances[i]:
                    distances[i] = distances[shortIndex] + matrix[shortIndex][i]
                    parent[i] = shortIndex

    finalpaths = []
    templist = []
    for i in range(len(matrix)):
        if i != office:
            getRoute(parent, i, route)
            # print(f"Path ({office} —> {i}): Minimum cost = {distances[i]}, Route = {route}")
            for q in range(len(route)):
                templist.append(locations[route[q]])
            finalpaths.append(list(templist))
            route.clear()
            templist.clear()
    finalDict = dict(zip(getLocations(map), finalpaths))
    return finalDict


# takes list of edges and returns a 2D list array
def getAdjacencyMap(edges):
    # build an adjacency matrix
    locations = getLocations(edges)
    numLocations = len(locations)
    # print(sorted(locations))

    # create 3D matrix
    nodeMap = [[-1] * numLocations for i in range(numLocations)]
    for u, v, weight in edges:
        index1 = locations.index(u)
        index2 = locations.index(v)

        nodeMap[index1][index2] = weight
        nodeMap[index2][index1] = weight
    # FOR CHECKING MATRIX
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


def getRoute(prev, i, route):
    if i >= 0:
        getRoute(prev, prev[i], route)
        route.append(i)
