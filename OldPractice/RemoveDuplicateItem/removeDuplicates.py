def removeDuplicates(self, nums):
    length = len(nums)
    i = 0
    while i < length-1:
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
            length -= 1
        else:
            i += 1
    return len(nums)