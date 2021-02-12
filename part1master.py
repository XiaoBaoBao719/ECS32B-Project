class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False

import math

def hash(id, tableSize):
        square = pow(id, 2)
        counter = 0
        middle = ""
        for i in str(square):
            if(counter == str(square) / 2):
                middle += i
            counter += 1
        return float(middle) % tableSize

class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = []

    def collectPackage(self, pk):
        # Push into some data structure, taking out of postal service
        if self.location == pk.address:
            self.append(pk.id)
        else:
            print("Truck is not at postal office!")

    def deliverOnePackage(self, pk):
        # Remove a singular package out of truck into delivery address
        if self.location == pk.address:
            self.pop(pk.id)
        else:
            print("Truck is not at the correct delivery address!")

    def deliverPackages(self):

        ##   Will remove multiple packages to a singluar address
        # Chained packages, so multiple packages
        # if self.location == pk.location:
        #     while
        if self.location == pk.address:
            while self.packages:
                self.packages.pop()
        else:
            print("Can not deliver packages")

    def removePackage(self, id, pk):
        if self.location == pk.location:
            self.pop(id, pk)
        else:
            print("Package has not returned to post office.")

    def driveTo(self, loc):
        if self.location != loc:
            self.location = loc
        else:
            print("Truck is already at destination")

    def getPackagesIds(self):
        self.packages.id()
