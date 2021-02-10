class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False

    

class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = []


    def collectPackage(self, pk):
        #Push into some data structure, taking out of postal service
        if self.location == pk.location:
            self.insert(pk)


    def deliverOnePackage(self, pk):


    def deliverPackages(self):
        

    def removePackage(self, pk):


    def driveTo(self, loc):


    def getPackagesIds(self):


