def removeDuplicates(self, nums):
    x = 0
    while(x < len(nums)-1):
        if nums[x] == nums[x+1]:
            nums.pop(x)
        else:
            x += 1
    return len(nums)
