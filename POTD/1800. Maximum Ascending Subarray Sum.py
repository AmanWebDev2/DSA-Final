'''
https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04
''''

'''
T.C -> O(n^2)
S.C -> O(1)
''''

def brute(nums:list[int]):
    result = 0
    n = len(nums)
    for i in range(n):
        sm = nums[i]
        for j in range(i+1,n):
            if nums[j] > nums[j-1]:
                sm += nums[j]
            else:
                break
        
        result = max(result,sm)
    return result

'''
T.C -> O(n)
S.C -> O(1)
'''

def optimal(nums:list[int]):
    n = len(nums)
    curr_sum = nums[0]
    max_sum = 0
    
    for i in range(1,n):
        if nums[i] > nums[i-1]:
            curr_sum += nums[i]
        else:
            max_sum = max(max_sum,curr_sum)
            curr_sum = nusm[i]

    return max(max_sum,curr_sum)
