# Problem descirption:
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

def SplitArrayBetweenPositiveAndNegative(listOfIntegers, numElements):
    numNonPositive = 0
    for i in range(0, numElements):
        if(listOfIntegers[i] < 1):
            listOfIntegers[i],listOfIntegers[numNonPositive] = listOfIntegers[numNonPositive], listOfIntegers[i]
            numNonPositive += 1
    return numNonPositive

def LowestPositiveIntergerNotPresent(listOfIntegers):
    numElements = len(listOfIntegers)
    nonPositives = SplitArrayBetweenPositiveAndNegative(listOfIntegers, numElements)

    return findTheNumber(listOfIntegers[nonPositives:], numElements - nonPositives )

def findTheNumber(listOfInts, length):
    for i in range(length):
        if(abs(listOfInts[i] - 1) < length and listOfInts[abs(listOfInts[i]) - 1] > 0):
            listOfInts[abs(listOfInts[i]) - 1] = -listOfInts[abs(listOfInts[i]) - 1]
    
    for i in range(length):
        if (listOfInts[i] > 0):
            return listOfInts[i] + 1
        
    return length + 1

def main():
    print("Testing with [3, 4, -1, 1]. Expected output: 2")
    print(LowestPositiveIntergerNotPresent([3, 4, -1, 1]))
    print("Testing with [1, 2, 0]. Expected output: 3")
    print(LowestPositiveIntergerNotPresent([1, 2, 0]))


main()