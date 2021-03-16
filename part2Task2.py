"""
Copy your Package and Truck classes here
"""
import math
from collections import defaultdict
from array import *
import math

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

    return sorted(uniqueLocations)
"""
BFS
"""
def bfs(map, office):
    #A DICTIONARY OF THE PATHS FROM SOURCE TO EACH UNIQUE DESTINATION
    mypaths = {}
    # for destination in getLocations(map):
    for destination in getLocations(map):
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
        self.packagesDelivered = [] * self.size

    def collectPackage(self, pk):
        print("COLLECTING")
        print(pk.id)
        print(pk.office)
        print(pk.collected)
        print(pk.delivered)
        print(self.location)

        if pk == None:
            print("No package to pick up!")
            return
        # Push into some data structure, taking out of postal service

        #curNumPkgs = len(getPackagesIds())
        #print(len(getPackagesIds()))

        curNumPkgs = 0

        for i in range(len(self.packages)):
            if self.packages[i] is not None:
                curNumPkgs += 1

        print("Curent num pkgs", curNumPkgs)

        index = hashMe(pk.id, len(self.packages))

        if self.location == pk.office:
            if(curNumPkgs < self.size):
                pk.collected = True
                self.packages[index] = pk
            else:
                print("Can't fit anymore packages")
            #self.packages[index].collected = True
        else:
            print("Truck is not at postal office!")

    def deliverOnePackage(self, pk):
        # Remove a singular package out of truck into delivery address
        print('DELIVERING ONE PACKAGES')
        index = hashMe(pk.id, tableDim)
        if self.location == pk.address and self.packages[index] is not None:
            self.packages[index].delivered = True
            self.packagesDelivered.append(pk.id)
            self.packages[index] = None
        else:
            print("Truck is not at the correct delivery address!")

    def deliverPackages(self):
        ##   Will remove multiple packages to a singular address
        # Chained packages, so multiple packages
        # if self.location == pk.location:
        print("Delivering LOTS OF PACKAGES")
        for i in range(len(self.packages)):
            if (self.packages[i] != None) and (self.location == self.packages[i].address):
                self.packages[i].delivered = True
                self.packagesDelivered.append(pk.id)
                self.packages[i] = None
        else:
            print("Can not deliver packages")

    def removePackage(self, pk):
        print("REMOVING A PACKAGE")
        print(pk.office)
        index = hashMe(pk.id, tableDim)
        if self.packages[index] is not None:
            self.packages[index].office = self.location
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

    def getPackagesIds(self):

        idList = []
        for i in range(len(self.packages)):
            if self.packages[i] is not None:
                idList.append(self.packages[i].id)

        return idList

    def getDeliveryDestinations(self):
		destinations = {()}

		for pkg in self.packages:
			print(pkg)
			destinations.add(pkg.address)
		return list(destinations)
"""
	def isDelivered(self, packId):
		if(packId in self.packagesDelivered):
			return True
		else:
			return False
"""
"""
deliveryService
"""
def deliveryService(map, truck, packages):
	deliveredTo = {}
	stops = []

    # write your code here
	theMap = getAdjacencyMap(map)
	theStops = getLocations(map)

    #Create Truck at location of UPS store
	print(truck.id, truck.size, truck.location)

	while (truck.packages <= truck.size):
			truck.collectPackage(packages.pop())

	print(truck.packages)
	#destinations = truck.getDeliveryDestinations()
	#print(destinations)

	while not truck.packages == []:

		#look at address for topmost package
		destination = truck.packages.peek().address
		#calculate a route to package address
		route = bfsHelper(map, truck.location, destination)

		#for each location along the route, move the truck and try to
		#deliver packages along the way
		for currentLocation in route:
			truck.driveTo(currentLocation)
			truck.deliverPackages()
			#check to see which packages were delivered and update the deliveredTo dict
			for package in truck.packages:
				if truck.isDelivered(package.id):
					deliveredTo.update({package.id : package.address})

			stops.append(currentLocation)

		print("Current packages: ", truck.packages)

	return (deliveredTo, stops)



#DRIVER CODE

m = [('UPS', 'Brecon', 3), ('Jacob City', 'Owl Ranch', 3), ('Jacob City', 'Sunfield', 15), ('Sunfield', 'Brecon', 25)]
o = 'UPS'
packages = [('pk1', 'UPS', 'Brecon'), ('pk2', 'UPS', 'Jacob City'), ('pk3', 'UPS', 'Owl Ranch'), ('pk4', 'UPS', 'Sunfield')]

truck = Truck(69, 20, o)
deliveryService(m, truck, packages)































