"""
https://leetcode.com/problems/contains-duplicate/description/
"""

nums = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

"""
T.C -> O(N^2)
S.C -> O(1)
"""


def brute(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# print(brute(nums))
# print(brute(nums2))
# print(brute(nums3))

"""
T.C -> O(N)
S.C -> O(N)
"""
from collections import defaultdict


def approach_1(nums: list[int]) -> bool:
    mpp = defaultdict(int)
    for num in nums:
        mpp[num] += 1
    for val in mpp.values():
        if val > 1:
            return True
    return False


# print(approach_1(nums))
# print(approach_1(nums2))
# print(approach_1(nums3))

"""
T.C -> O(N)
S.C -> O(N)
"""


def approach_2(nums: list[int]) -> bool:
    if len(set(nums)) == len(nums):
        return False
    return True


print(approach_2(nums))
print(approach_2(nums2))
print(approach_2(nums3))
