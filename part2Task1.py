import heapq
from collections import defaultdict
import math
"""
BFS
"""


# def bfs(map, office):
#     adjacencyList = helpAdjList(map)
#
#     visitstatus = {}
#     mypaths = []
#     myqueue = []
#     myqueue.append(office)
#
#     visitstatus[office] = True
#
#     for i in adjacencyList:
#         key = i[0]
#         visitstatus.append({key: False})
#
#     print(visitstatus)
#
#     while myqueue:
#         office = myqueue.pop(0)
#
#         for nextnode in map[office]:
#             if visitstatus[nextnode] == False:
#                 myqueue.append(nextnode)
#                 visitstatus[nextnode] = True
#
#     return mypaths


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
    # distances[office] = 0
    #
    # pq = [(0, office)]
    # while pq:  # while pq is not empty
    #     curDist, curVert = heapq.heappop((pq))  # current distance and current vertex
    #
    #     while curDist > distances[curVert]:
    #         for nextNode, weight in map[curVert].items():
    #             distance = curDist + weight
    #
    #             if distance < distances[nextNode]:
    #                 distances[nextNode] = distance
    #                 heapq.heappush()
    #
    # return distances

    row = len(map)
    col = len(map[0])

    mydistance = {}
    # Initializing distances as infinity
    mydistance = [math.inf] * row

    # Storing shortest path to tree
    parent = [-1] * row

    #Assigning distance of post office to itself (source node) as zero
    mydistance[office] = 0

    myqueue = []
    for i in range(row):
        queue.append(i)

    while myqueue:
        u = shortestDist(mydistance, myqueue)

        # remove min element
        myqueue.remove(u)

        for i in range(col):
            # Relaxation
            if map[u][i] and i in myqueue:
                if dist[u] + map[u][i] < dist[i]:
                    dist[i] = dist[u] + map[u][i]
                    parent[i] = u

    return parent


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


def shortestDist(distance, queue):
    minval = float("Inf")
    minvalIndex = -1

    for i in range(len(distance)):
        if dist[i] < minval and i in queue:
            minval = dist[i]
            minvalIndex = i
        return minvalIndex


m = [('UPS', 'Brecon', 3), ('Jacob City', 'Owl Ranch', 3), ('Jacob City', 'Sunfield', 15), ('Sunfield', 'Brecon', 25)]
val = dijkstra(m, 'UPS')

print(dijkstra(m, val))