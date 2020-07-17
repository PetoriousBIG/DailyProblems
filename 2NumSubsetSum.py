# Problem Description:
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def twoNumSubsetSum(numList, k):
    numList.sort()
    leftIndex = 0
    rightIndex = len(numList) - 1
    while(True):
        if leftIndex > rightIndex:
            return False
        
        possibleK = numList[leftIndex] + numList[rightIndex]
        if possibleK == k:
            return True
        elif possibleK > k:
            rightIndex -= 1
        else:
            leftIndex += 1


def main():
    print('Testing [1, 3, 2, 4, 7, 6, 5], 10; should return True')
    print(twoNumSubsetSum([1, 3, 2, 4, 7, 6, 5], 10))

    print('Testing [10, 55, 62, 35, 7, 90, 34], 8; should return False')
    print(twoNumSubsetSum([10, 55, 62, 35, 7, 90, 34], 8))

main()