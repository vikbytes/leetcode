def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for x in range(len(nums)):
        y = x+1
        while(y<len(nums)):
            if nums[x]+nums[y] == target:
                return [x, y]
            else:
                y += 1
                    
print(twoSum([2,7,11,15], 9))