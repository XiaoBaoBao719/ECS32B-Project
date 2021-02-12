import math

def hash(id, tableSize):

    nums2 = 0

    if isinstance(id, str):
        for i in id:
          nums2 += ord(i)
    else:
        nums2 = id

    square = pow(nums2, 2)
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

size = 1000
id = "pk1"

print(hash(id, size))



#print(math.log(100, 10))