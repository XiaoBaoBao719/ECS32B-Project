import math

def hash(id, tableSize):
    square = pow(id, 2)
    counter = 0
    middle = ''
    squared = str(square)
    distFromMiddle = int(math.log(tableSize, 10))

    #print(square)
    #print(squared)

    middleIndex = int((len(squared) / 2))
    fwd = middleIndex - distFromMiddle + 1
    bwd = middleIndex + distFromMiddle

    middleNums = str(int(squared[fwd:bwd]))
    #print(middleNums)
    #middle = int(middle) % tableSize
    #print(middle)

    #return middle


    return int(middleNums) % tableSize


"""THIS IS A TEST AREA """

size = 100
id = 144

print(hash(id, size))

#print(math.log(100, 10))