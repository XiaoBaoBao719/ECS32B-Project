import math


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
        self.packages = [None] * 20

    def collectPackage(self, pk):
        print(pk.id)
        if pk == None:
            print("No package to pick up!")
        # Push into some data structure, taking out of postal service
        index = hashMe(pk.id, len(self.packages))
        if self.location == pk.office:
            pk.collected = True
            self.packages[index] = pk
        else:
            print("Truck is not at postal office!")

    def deliverOnePackage(self, pk):
        # Remove a singular package out of truck into delivery address
        print('DELIVERING ONE PACKAGES')
        index = hashMe(pk.id, tableDim)
        if self.location == pk.address and self.packages[index] is not None:
            self.packages[index].delivered = True
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
            #     for j in range(len(idList)):
            #         while self.packages[i] is not None:
            #             idList[j] = self.packages[i].id
            #             i += 1
            #         j += 1
            if self.packages[i] is not None:
                idList.append(self.packages[i].id)

        # idList = [self.packages[i].id for i in range(len(self.packages))]
        return idList
