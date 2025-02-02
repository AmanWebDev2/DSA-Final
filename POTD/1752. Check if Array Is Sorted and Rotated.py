'''
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2025-02-02
'''


'''
T.C -> O(n^2)
S.C -> O(n)
'''

def check_brute(nums:list[int]) -> bool:
    n = len(nums)
    sorted_arr = [0] * n
    for r in range(n):
        idx = 0
        
        for i in range(r,n):
            sorted_arr[idx] = nums[i]
            idx += 1
        
        for j in range(0,r):
            sorted_arr[idx] = nums[j]
            idx += 1
        
        # check if array is sorted or not
        is_sorted = True
        for k in range(1,n):
            if sorted_arr[k] < sorted_arr[k-1]:
                is_sorted = False
                break
        
        if is_sorted:
            return True
    
    return False


'''
T.C -> O(n^2) + O(nlogn)
S.C -> O(n)
'''
def check_better_brute(nums:list[int]):
    n = len(nums)
    sorted_arr = sorted(nums)
    for r in range(n):
        is_sorted = True
        for i in range(n):
            if sorted_arr[i] != nums[(i+r) %n]:
                is_sorted = False
                break
        if is_sorted:
            return True
    return False


def check_optimal(nums:list[int]):
    n = len(nums)
    peak = 0
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            peak += 1
    return False if peak > 1 else True