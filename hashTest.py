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


size = 10
id = 44

print(hash(id, size))