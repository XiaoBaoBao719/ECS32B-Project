"""
Copy your Package and Truck classes here
"""
import math
from collections import defaultdict
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
    #print(locations)
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

def dijkstra(map, office, destination): #now taking a destination path
    matrix = getAdjacencyMap(map)
    locations = getLocations(map)

    row = len(matrix)
    col = len(matrix[0])

    #distances = [math.inf] * row
    distances = [float('inf')] * row
    parent = [-1] * row

    officeIndex = getLocations(map).index('UPS')  # Setting office distance from itself equal to zero
    distances[officeIndex] = 0

    myqueue = []
    for i in range(row):
        myqueue.append(i)
    route = []
    while myqueue:
        #shortDist = math.inf  # shortest distance
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
        #if i != office and distances[i] != math.inf:
        if i != office and distances[i] != float('inf'):
            get_route(parent, i, route)
            for q in range(len(route)):
                templist.append(locations[route[q]])
            finalpaths.append(list(templist))
            #route.clear()
            del route[:]
            #templist.clear()
            del templist[:]
    #print(finalpaths)

    finalDict = dict(zip(getLocations(map), finalpaths))

    shortPathDest = finalDict[destination]
    #print(shortPathDest)
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

"""
@parameter id - integer value number that represents the package tracking number
           tableSize - the size of the hash table 
@precondition: both id and tableSize must be integer values
@return: method returns an integer value i such that 0 <= i <= tableSize
"""

def hashMe(id, tableSize):
    nums2 = 0

    # checks if a string, uses ord() to convert string into int
    if isinstance(id, str):
        for i in id:
            nums2 += ord(i)
    else:
        nums2 = id

    square = pow(nums2, 2)
    counter = 0
    middle = ''

    # converts id into a string
    squared = str(square)

    # calculates the number of place digits to pick relative to the middle digit
    distFromMiddle = int(math.log(tableSize, 10))

    # gets the middle digit index
    middleIndex = int((len(squared) / 2))

    # gets the beginning the middle digits
    fwd = middleIndex - distFromMiddle + 1

    # gets the end of the middle digits
    bwd = middleIndex + distFromMiddle

    # gets the middle digits
    middleNums = str(int(squared[fwd:bwd]))

    # Returns index (key)
    return int(middleNums) % tableSize


tableDim = 20


class Truck:

    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = [None] * self.size
        self.packagesDelivered = [False] * self.size

    def collectPackage(self, pk):
        print("COLLECTING")
        #print(pk.id)
        #print(pk.office)
        #print(pk.collected)
        #print(pk.delivered)
        #print(self.location)

        if pk == None:
            print("No package to pick up!")
            return
        # Push into some data structure, taking out of postal service

        # curNumPkgs = len(getPackagesIds())
        # print(len(getPackagesIds()))

        curNumPkgs = 0

        for i in range(len(self.packages)):
            if self.packages[i] is not None:
                curNumPkgs += 1

        print("Curent num pkgs", curNumPkgs)

        index = hashMe(pk.id, len(self.packages))

        if self.location == pk.office:
            if (curNumPkgs < self.size):
                pk.collected = True
                self.packages[index] = pk
                self.packagesDelivered[index] = False
            else:
                print("Can't fit anymore packages")
            # self.packages[index].collected = True
        else:
            print("Truck is not at postal office!")

    def deliverOnePackage(self, pk):
        # Remove a singular package out of truck into delivery address
        print('DELIVERING ONE PACKAGES')
        index = hashMe(pk.id, tableDim)
        if self.location == pk.address and self.packages[index] is not None:
            self.packagesDelivered[index] = True
            #self.packagesDelivered.append(pk.id)
            self.packages[index] = None
        else:
            print("Truck is not at the correct delivery address!")

    def deliverPackages(self):
        ##   Will remove multiple packages to a singular address
        # Chained packages, so multiple packages
        # if self.location == pk.location:
        print("Delivering LOTS OF PACKAGES")
        for i in range(len(self.packages)):
            if (self.packages[i] != None) and (
                    self.location == self.packages[i].address):  # updating (self.location == self.packages[i].address)
                self.packagesDelivered[i] = True
                #self.packagesDelivered.append(self.packages.id)
                self.packages[i] = None
        else:
            print("Can not deliver packages")

    def removePackage(self, pk):
        print("REMOVING A PACKAGE")
        print(pk.office)
        index = hashMe(pk.id, tableDim)
        if self.packages[index] is not None:
            self.packages.office[index] = self.location #updating self.packages[index].office = self.location -Gianni
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
                idList.append(self.packages[i].id) #updating idList.append(self.packages[i].id)

        return idList

    def getDeliveryDestinations(self):
        destinationsList = []
        for i in range(len(self.packages)):
            if self.packages[i] is not None:

                print(self.packages[i].address)

                destinationsList.append(self.packages[i].address) #updating idList.append(self.packages[i].id)
        return destinationsList

    def isDelivered(self, packId):
        index = hashMe(packId, tableDim)
        return self.packagesDelivered[index]

    def getNumPackages(self):
        counter = 0
        for i in self.packages:
            if(i is not None):
                counter += 1
        return counter
    #def getPackage()

"""
deliveryService
"""

def deliveryService(map, truck, packages):
    deliveredTo = {}
    stops = []

    # write your code here
    theMap = getAdjacencyMap(map)
    theLocations = getLocations(map)

    # Create Truck at location of UPS store
    #print(truck.id, truck.size, truck.location)
    startLocation = truck.location

    #packIds = []
    deliveredPackages = []

    #The [:]  operation copies list by value instead of by reference
    undeliveredPackages = packages[:]
    #print(undeliveredPackages.pop())

    #truck.collectPackage(undeliveredPackages.pop())

    #while (truck.getNumPackages() <= truck.size):
    #    if(undeliveredPackages):
    #        truck.collectPackage(undeliveredPackages.pop())


    #print(truck.packages)
    
    while undeliveredPackages:

        #PICK UP AS MANY UNDELIVERED PACKAGES AS TRUCK CAN HOLD
        while (truck.getNumPackages() <= truck.size):
            if(undeliveredPackages):
                curPack = undeliveredPackages.pop()
                #packIds.append(curPack.id)
                truck.collectPackage(curPack)
            else:
                break

        print(truck.packages)

        allDestinations = truck.getDeliveryDestinations()
        allPackageIds = truck.getPackageIds()
        
        #AS LONG AS THERE ARE PACKAGES IN TRUCK...
        while allDestinations:


            print("NUM PACKS: ", truck.getNumPackages())
            #GET THE TOPMOST PACKAGE ADDRESS, BLIND DRIVING
            #Blindly Drive somewhere
            destination = allDestinations.pop()

            #CALCULATE THE ROUTE TO DESTINATION
            route = dijkstra(map, truck.location, destination)

            #AT EACH CITY:
            #-DRIVE TO CITY
            #-DELIVER PACKAGES TO CURRENT CITY
            #-LOOP THROUGH PACKAGE LIST AND UPDATE deliveredTo SO WE KNOW WHAT HAS BEEN DELIVERED
            for currentCity in route:
                truck.driveTo(currentCity)
                truck.deliverPackages()

                #REMOVE CITY FROM DESTINATIONS LIST SINCE WE ARE VISITING AND DELIVERING
                if currentCity in allDestinations:
                    allDestinations.remove(currentCity)

                # check to see which packages were delivered and update the deliveredTo dict
                for packId in allPackageIds:
                    if truck.isDelivered(packId):
                        deliveredTo.update({packId: currentCity})
                        deliveredPackages.append(packId)
                        allPackageIds.remove(packId)
                stops.append(currentCity)

            print("Current packages: ", truck.packages)

        #GO BACK TO POST OFFICE TO GET MORE PACKAGES
        routeOffice = dijkstra(map, truck.location, startLocation)
        #DROP OFF PACKAGES THAT HAVE NOT BEEN DELIVERED
        for packId in allPackageIds:
            truck.removePackage(packId)


    print("FINAL OUTPUT", deliveredTo, stops)
    return (deliveredTo, stops)


# DRIVER CODE

m = [('UPS', 'Brecon', 3), ('Jacob City', 'Owl Ranch', 3), ('Jacob City', 'Sunfield', 15), ('Sunfield', 'Brecon', 25)]
o = 'UPS'

pk1 = Package('pk1')
pk1.address = 'Brecon'
pk2 = Package('pk2')
pk2.address = 'Jacob City'
pk3 = Package('pk3')
pk3.address = 'Owl Ranch'
pk4 = Package('pk4')
pk4.address = 'Sunfield'

packages = [pk1, pk2, pk3, pk4]

for i in packages:
    i.office = 'UPS'

#print(packages)

truck = Truck(69, 20, o)
deliveryService(m, truck, packages)

