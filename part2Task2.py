"""
Copy your Package and Truck classes here
"""
import math
from collections import defaultdict

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


def getAdjacencyMap(edges):
    nodeMap = [[], []]
    # build an adjacency matrix
    locations = getLocations(edges)
    numLocations = len(locations)
    # print(sorted(locations))

    # create 3D matrix
    nodeMap = [[-1] * numLocations for i in range(numLocations)]
    # print(nodeMap)
    for u, v, weight in edges:
        #    print(u)
        #    print(v)
        #    print(weight)
        index1 = locations.index(u)
        index2 = locations.index(v)

        nodeMap[index1][index2] = weight
        nodeMap[index2][index1] = weight
    # print(locations)
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

    return sorted(uniqueLocations)


"""
Dijkstra's
"""


def dijkstra(map, office, destination):  # now taking a destination path
    matrix = getAdjacencyMap(map)
    locations = getLocations(map)

    row = len(matrix)
    col = len(matrix[0])

    # distances = [math.inf] * row
    distances = [float('inf')] * row
    parent = [-1] * row

    officeIndex = getLocations(map).index('UPS')  # Setting office distance from itself equal to zero
    distances[officeIndex] = 0

    myqueue = []
    for i in range(row):
        myqueue.append(i)
    route = []
    while myqueue:
        # shortDist = math.inf  # shortest distance
        shortDist = float('inf')
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
        # if i != office and distances[i] != math.inf:
        if i != office and distances[i] != float('inf'):
            get_route(parent, i, route)
            for q in range(len(route)):
                templist.append(locations[route[q]])
            finalpaths.append(list(templist))
            # route.clear()
            del route[:]
            # templist.clear()
            del templist[:]
    # print(finalpaths)

    finalDict = dict(zip(getLocations(map), finalpaths))

    shortPathDest = finalDict[destination]
    # print(shortPathDest)
    return shortPathDest


def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)


class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""  # Delivery address
        self.office = ""  # Post office address
        self.ownerName = ""
        self.collected = False
        self.delivered = False


class Truck:

    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = [None] * self.size
        self.packagesDelivered = [False] * self.size

    def hashMe(self, id):

        index = 0

        if isinstance(id, str):
            for i in id:
                index += ord(i)

        print(type(index))
        index = index % self.size

        while self.packages[index] is not None and self.packages[index] != id:
            index = (index + 1) % self.size
        return index

    def collectPackage(self, pk):
        print("COLLECTING")
        # print(pk.id)
        # print(pk.office)
        # print(pk.collected)
        # print(pk.delivered)
        # print(self.location)

        if pk == None:
            print("No package to pick up!")
            return
        # Push into some data structure, taking out of postal service

        # curNumPkgs = len(getPackagesIds())
        # print(len(getPackagesIds()))

        curNumPkgs = 0

        print("NOW INSERTING ", pk)

        for i in range(len(self.packages)):
            print("CHECKING NUM PACKAGES", self.packages[i])

            if self.packages[i] is not None:
                curNumPkgs += 1

        print("Curent num pkgs", curNumPkgs)

        index = self.hashMe(pk.id)

        if self.location == pk.office:
            if (curNumPkgs < self.size):
                pk.collected = True
                self.packages[index] = pk
                print(self.packages)
                self.packagesDelivered[index] = False
            else:
                print("Can't fit anymore packages")
            # self.packages[index].collected = True
        else:
            print("Truck is not at postal office!")

    def deliverOnePackage(self, pk):
        # Remove a singular package out of truck into delivery address
        print('DELIVERING ONE PACKAGES')
        index = self.hashMe(pk.id)
        if self.location == pk.address and self.packages[index] is not None:
            self.packagesDelivered[index] = True
            # self.packagesDelivered.append(pk.id)
            self.packages[index] = None
        else:
            print("Truck is not at the correct delivery address!")

    def deliverPackages(self):
        ##   Will remove multiple packages to a singular address
        # Chained packages, so multiple packages
        # if self.location == pk.location:
        print("Delivering LOTS OF PACKAGES")

        for i in range(len(self.packages)):
            #print(self.location + " Line 266")
            #currentPackage = self.packages[i]
            # print(currentPackage, self.packages.address)
            if (self.packages[i] is not None) and (self.location == getattr(self.packages[i], 'address')):
                # self.packages[i].address):
                #print(getattr(self.packages[i], 'address') + " Line 271")
                #print(getattr(self.packages[i], 'address'))
                self.packagesDelivered[i] = True
                print(self.packagesDelivered)
                # self.packagesDelivered.append(self.packages.id)
                self.packages[i] = None
            if self.packages[i] == None:
                print("I can not deliver a none-existent package")
            else:
                print("Can not deliver packages")


    def removePackage(self, pk):
        print("REMOVING A PACKAGE")
        print(pk.office)
        index = self.hashMe(pk.id)
        if self.packages[index] is not None:
            self.packages.office[index] = self.location  # updating self.packages[index].office = self.location -Gianni
            pk.delivered = False
            pk.collected = False
            self.packages[index] = None
        else:
            print("Package has not returned to post office.")


    def driveTo(self, loc):
        if self.location != loc:
            self.location = loc
        else:
            print("Truck is already at destination")


    def getPackageIds(self):
        idList = []
        for i in range(len(self.packages)):
            if self.packages[i] is not None:
                idList.append(getattr(self.packages[i], "id"))#(self.packages[i].id)  # updating idList.append(self.packages[i].id)

        return idList


    def getDeliveryDestinations(self):
        destinationsList = []
        for i in range(len(self.packages)):
            if self.packages[i] is not None:
                print(getattr(self.packages[i], 'address'))# (self.packages[i].address + " is the city")
                destinationsList.append(getattr(self.packages[i], 'address'))#(self.packages[i].address)  # updating idList.append(self.packages[i].id)
        return destinationsList


    def isDelivered(self, packId):
        index = self.hashMe(packId)
        return self.packagesDelivered[index]


    def getNumPackages(self):
        counter = 0
        for i in self.packages:
            if (i is not None):
                counter += 1
        return counter

"""
deliveryService
"""
def ComputeAdj(map):
    adj = defaultdict(list)

    counter = 0
    for item in map:
        adj[counter] = [item]
        counter += 1

    for key in adj.getKeys():
        sorted(adj[key])

    return adj

def sortpackagesbyoffice(packages):
    pkgsByOffice = defaultdict(list)

    for pkg in packages:
        pkgsByOffice[pkg.office].append(pkg)

    return pkgsByOffice

def findPath(map, start, destination):  # using BFS
    mypaths = {}
    # for i in getLocations(map):

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
            validPath = currentPath

        adjVertices = []
        for i in adjIndices:
            adjVertices.append(getLocations(map)[i])

        for adjacent in adjVertices:
            if (adjacent not in visited):
                newPath = list(currentPath)
                newPath.append(adjacent)
                myqueue.append(newPath)
        mypaths.update({destination: validPath})

    return mypaths

def followpath(path, stop, truck):
    if path == [] or truck.location != path[0]:
        return
    for place in path:
        truck.driveTo(place)
        stop.append(place)


def completeDriveThrough(truck, adj, destination, stop):
    path = findPath(adj, truck.location, destination)
    followpath(path, stop, truck)



def deliveryService(map, truck, packages):
    """
    deliveredTo = {}
    stops = []

    # write your code here
    theMap = getAdjacencyMap(map)
    theLocations = getLocations(map)

    # Create Truck at location of UPS store
    # print(truck.id, truck.size, truck.location)
    startLocation = truck.location

    # packIds = []
    deliveredPackages = []

    # The [:]  operation copies list by value instead of by reference
    undeliveredPackages = packages[:]
    # print(undeliveredPackages.pop())

    # truck.collectPackage(undeliveredPackages.pop())

    # while (truck.getNumPackages() <= truck.size):
    #    if(undeliveredPackages):
    #        truck.collectPackage(undeliveredPackages.pop())

    # print(truck.packages)

    while undeliveredPackages:

        # PICK UP AS MANY UNDELIVERED PACKAGES AS TRUCK CAN HOLD
        while truck.getNumPackages() < truck.size:
            if undeliveredPackages:
                curPack = undeliveredPackages.pop()
                # packIds.append(curPack.id)
                truck.collectPackage(curPack)
            else:
                break

        print(truck.packages)

        allDestinations = truck.getDeliveryDestinations()
        allPackageIds = truck.getPackageIds()

        # AS LONG AS THERE ARE PACKAGES IN TRUCK...
        while allDestinations:

            print("NUM PACKS: ", truck.getNumPackages())
            # GET THE TOPMOST PACKAGE ADDRESS, BLIND DRIVING
            # Blindly Drive somewhere
            destination = allDestinations.pop()

            # CALCULATE THE ROUTE TO DESTINATION
            route = dijkstra(map, truck.location, destination)

            # AT EACH CITY:
            # -DRIVE TO CITY
            # -DELIVER PACKAGES TO CURRENT CITY
            # -LOOP THROUGH PACKAGE LIST AND UPDATE deliveredTo SO WE KNOW WHAT HAS BEEN DELIVERED
            for currentCity in route:
                truck.driveTo(currentCity)
                truck.deliverPackages()
                print(currentCity)
                # REMOVE CITY FROM DESTINATIONS LIST SINCE WE ARE VISITING AND DELIVERING
                if currentCity in allDestinations:
                    allDestinations.remove(currentCity)

                # check to see which packages were delivered and update the deliveredTo dict
                for packId in allPackageIds:

                    #print(packId)
                    #print(truck.isDelivered(packId))
                    if truck.isDelivered(packId):
                        deliveredTo.update({packId: currentCity})  # "Stamped Delivered"
                        deliveredPackages.append(packId)  # updates the delivered packages list
                        allPackageIds.remove(packId)  # remove package from package ids
                stops.append(
                    currentCity)  # after done with all package delivery operations in current city, we mark that
                # we have visited the city

            print("Current packages: ", truck.packages)

        # GO BACK TO POST OFFICE TO GET MORE PACKAGES
        routeOffice = dijkstra(map, truck.location, startLocation)
        # DROP OFF PACKAGES THAT HAVE NOT BEEN DELIVERED
        for packId in allPackageIds:
            truck.removePackage(packId)  # must clean up how to offload packages to office
    """
    stops = []
    deliveredTo = {}
    AdjMap = ComputeAdj(map)

    sortedPkgs = sortpackagesbyoffice(packages)
    stops = [[truck.location]]

    for office in sortedPkgs:

        packagesNeeded = sortedPkgs[office]
        completeDriveThrough(truck, map, office, stops)

        while packagesNeeded and truck.getNumPackages() < truck.size:
            package = packagesNeeded.pop()
            truck.collectPackage(package)

        while truck.packages:
            pkg = truck.packages.pop(0)
            addressToVisit = pkg[0].address
            completeDriveThrough(truck, map, addressToVisit, stops)

            for pkg in truck.packages:
                if pkg.address == addressToVisit:
                    truck.deliveredPackages(pkg)
                    deliveredTo.add(pkg.id, pkg.address)


        completeDriveThrough(truck, map, office, stops)

    
    print("FINAL OUTPUT", deliveredTo, stops)
    return (deliveredTo, stops)


