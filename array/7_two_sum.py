"""
T.C -> O(n^2)
S.C -> O(1)
"""

nums = [3, 2, 4]
target = 6

nums = [2, 7, 11, 15]
target = 9


def brute(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def approach_map(nums: list[int], target: int) -> list[int]:
    mpp = dict()
    for i, num in enumerate(nums):
        rem = target - num
        if mpp.get(rem) is None:
            mpp[num] = i
        else:
            return [mpp.get(rem), i]


print(brute(nums, target))
print(approach_map(nums, target))
