"""
T.C -> O(n)
S.C -> O(1)
"""


def left_rotate_one_place(nums: list[int]):
    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]

    nums[-1] = temp


arr = [1, 2, 3, 4, 5]
left_rotate_one_place(arr)
print(arr)
