def singleNumber(nums):
    temp = nums[0]
    
    for x in range(1,len(nums)):
        if nums[x] == temp:
