# Given an array of integers and a number k, find maximum sum of a subarray of size k.

# Examples : 
# Input  : arr[] = {100, 200, 300, 400}
#          k = 2
# Output : 700

# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
#          k = 4 
# Output : 39

def maxSumSubarrayOfSizeK(nums, k):
    numsLength = len(nums)
    if k > numsLength:
        return None
    subarray = nums[0: k]
    max = sum(subarray)

    for i in range(k, numsLength):
        possibleMax = max
        posToReplace = i % k
        possibleMax -= subarray[posToReplace]
        subarray[posToReplace] = nums[i]
        possibleMax += nums[i]
        if possibleMax > max:
            max = possibleMax

    return max

def main():
    
    print("Testing [100, 200, 300, 400] with size 2. Expected output is 700")
    print(str(maxSumSubarrayOfSizeK([100, 200, 300, 400], 2)))

    print("Testing [100, 200, 300, 400] with size 2. Expected output is 39")
    print(str(maxSumSubarrayOfSizeK([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)))

    print("Testing [1, 2, 3, 4, 5] with size 6. Expected output is None")
    print(str(maxSumSubarrayOfSizeK([1, 2, 3, 4, 5], 6)))



main()