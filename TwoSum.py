def twoSum(nums, target):

    Hash = {} #Hashmap that will store passed values
        
    for index, num in enumerate(nums):
        difference = target - num
        if difference in Hash:
            return [Hash[difference], index]
        Hash[num] = index

testcase = [10, 6, 4, 9, 199, 1]  

print(twoSum(testcase, 200))
print(twoSum(testcase, 13))
print(twoSum(testcase, 11))
print(twoSum(testcase, 15))
