import math

class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False

"""
@parameter id - integer value number that represents the package tracking number
           tableSize - the size of the hash table 
@precondition: both id and tableSize must be integer values
@return: method returns an integer value i such that 0 <= i <= tableSize
"""
def hash(id, tableSize):
    #squares the id
    square = pow(id, 2)
    counter = 0
    middle = ''
    
    #converts id into a string
    squared = str(square)

    #calculates the number of place digits to pick relative to the middle digit
    distFromMiddle = int(math.log(tableSize, 10))

    #gets the middle digit index
    middleIndex = int((len(squared) / 2))

    #gets the beginning the middle digits
    fwd = middleIndex - distFromMiddle + 1

    #gets the end of the middle digits
    bwd = middleIndex + distFromMiddle

    #gets the middle digits
    middleNums = str(int(squared[fwd:bwd]))

    return int(middleNums) % tableSize

class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = {}

     def collectPackage(self, pk):
        # Push into some data structure, taking out of postal service
        index = hash(pk.id, self.packages.size)

        if self.location == pk.address:
            self.append(pk)
            pk.collected = True
        else:
            print("Truck is not at postal office!")

     def deliverOnePackage(self, pk):
        # Remove a singular package out of truck into delivery address
        if self.location == pk.address:
            self.remove(pk)
            pk.delivered = True
        else:
            print("Truck is not at the correct delivery address!")
            
     def deliverPackages(self):
        ##   Will remove multiple packages to a singular address
        # Chained packages, so multiple packages
        # if self.location == pk.location:
        #     while
        while self.packages:
            self.packages.pop()
        else:
            print("Can not deliver packages")

     def removePackage(self, pk):
        if self.location == pk.address:
            self.packages.pop(pk)
        else:
            print("Package has not returned to post office.")

    def driveTo(self, loc):
        if self.location != loc:
            self.location = loc
        else:
            print("Truck is already at destination")

    def getPackagesIds(self):
        self.packages.id()
