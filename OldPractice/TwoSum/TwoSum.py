# https://leetcode.com/problems/two-sum/
# This one returns the indices
def twoSum(nums, target):
    Hash = {} #Hashmap that will store passed values

    for index, num in enumerate(nums):
        difference = target - num
        if difference in Hash:
            return [Hash[difference], index]
        Hash[num] = index

# https://www.algoexpert.io/questions/Two%20Number%20Sum
# This one returns the nums needed
def twoNumberSum(array, targetSum):
    nums = {} # Creating an empty hashmap
    for num in array: # Iterating through array
        potentialmatch = targetSum - num # New variable that will take the nums
        if potentialmatch in nums:
            return [potentialmatch, num]
        else:
            nums[num] = None
    return []
