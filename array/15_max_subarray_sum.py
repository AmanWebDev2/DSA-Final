import math

def brute(nums:list[int]):
    n = len(nums)
    max_sum = -math.inf
    for i in range(n):
        for j in range(i,n):
            subarray = nums[i,j+1]
            max_sum = max(max_sum,sum(subarray))
    return max_sum

def better_brute(nums:list[int]):
    n = len(nums)
    max_sum = -math.inf
    for i in range(n):
        subarray_sum = 0
        for j in range(i,n):
            subarray_sum += nums[j]
            max_sum = max(subarray_sum,max_sum)
    return max_sum

def better(nums:list[int]):
    curr_sum = 0
    max_sum = -math.inf
    for num in nums:
        curr_sum += num
        max_sum = max(max_sum,curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum
