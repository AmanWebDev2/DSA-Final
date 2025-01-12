'''
T.C -> O(n^2)
S.C -> O(n)
'''

def brute(nums:list[int])->int:
    store = set(nums)
    max_streak = 0
    for num in nums:
        streak,curr = 0,num
        while curr in store:
            streak += 1
            curr += 1
        max_streak = max(max_streak,streak)
    return max_streak


'''
T.C -> O(n) + O(nlogn)
S.C -> O(1)
'''

def longest_consecutive(nums:list[int]) -> int:
    # length == 0
    if not nums:
        return 0

    nums.sort()
    max_streak = streak = 1

    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            continue
        
        if nums[i] == nums[i-1] + 1:
            streak += 1
        else:
            streak = 1
        max_streak = max(max_streak,streak)
    return max_streak


def optimal(nums:list[int])->int:
    store = set(nums)
    streak = max_streak = 0
    for num in store:
        if num - 1 in store:
            continue
        streak = 1
        while num + streak in store:
            streak += 1
        max_streak = max(max_streak,streak)
    return max_streak