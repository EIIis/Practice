# https://leetcode.com/problems/rotate-array/

def rotate(nums, k):

    if k % len(nums) == 0:
        return nums

    for i in range(0, k):
        prev = nums[len(nums) - 1]
        for j in range(len(nums) - 1, -1, -1):
            nums[j] = nums[j-1]
        nums[0] = prev
    return nums


test = [4, 5, 7, 2, 6, 1]
print(rotate(test, 3))
