'''
https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/?envType=daily-question&envId=2025-02-03
'''

'''
T.C -> O(n^2)
S.C -> O(1)
'''

def brute(nums:list[int]):
    n = len(nums)
    max_length = 1
    
    # Find longest strictly increasing subarray
    for i in range(n):
        curr_len = 1
        for j in range(i+1,n):
            # Extend subarray if next element is larger
            if nums[j] > nums[j-1]:
                curr_len += 1
            else:
            # Break if sequence is not increasing anymore
                break
        
        max_length = max(max_length,curr_len)

    # Find longest strictly decreasing subarray
    for i in range(n):
        curr_len = 1
        for j in range(i+1,n):
            # Extend subarray if next element is smaller
            if nums[j] < nums[j-1]:
                curr_len += 1
            else:
                # Break if sequence is not decreasing anymore
                break

        max_length = max(max_length,curr_len)

    return max_length

'''
T.C -> O(n)
S.C -> O(1)
'''
def optimal(nums:list[int]):
    n = len(nums)
    inc_len = dec_len = max_len = 1
    for i in range(n-1):
        if nums[i+1] > nums[i]:
            inc_len += 1
            dec_len = 1
        elif nums[i+1] < nums[i]:
            dec_len += 1
            inc_len = 1
        else:
            inc_len = 1
            dec_len = 1
        max_len = max(max_len,inc_len,dec_len)
    return max_len