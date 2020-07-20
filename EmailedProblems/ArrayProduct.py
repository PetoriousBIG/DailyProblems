# Problem Description
# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i. For example, if our 
# input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?
#

def arrayOfProductsOfElements(list):
    product = 1
    returnList = []
    for num in list:
        product *= num

    for num in list:
        returnList.append(product/num)

    return returnList

def arrayOfProductsOfElementsNoDivision(list):
    numElements = len(list)
    leftOfI = [1]
    rightOfI = [1]
    returnList = []
    for i in range(1, numElements):
        leftOfI.append(list[i-1]*leftOfI[i-1])
    for i in range(numElements - 1, 0, -1):
        rightOfI.insert(0, list[i] * rightOfI[0])
    for i in range(0, numElements):
        returnList.append(leftOfI[i] * rightOfI[i])

    return returnList

def main():
    print("Testing with division [1, 2, 3, 4, 5]; Expected answer: [120, 60, 40, 30, 24]")
    print(arrayOfProductsOfElements([1, 2, 3, 4, 5]))

    print("Testing without division [1, 2, 3, 4, 5]; Expected answer: [120, 60, 40, 30, 24]")
    print(arrayOfProductsOfElementsNoDivision([1, 2, 3, 4, 5]))
main()