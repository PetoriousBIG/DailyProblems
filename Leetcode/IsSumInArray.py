# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example 
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # solution that converts the array to a hashmap
        # mapping the value of the array to its index

        # for a number in the array, search the dictionary for
        # number needed to sum to target
        
        dict = {}
        for i in range(0, len(nums)):
            neededToSum = target - nums[i]
            if neededToSum in dict:
                return [dict[neededToSum], i]
            dict[nums[i]] = i