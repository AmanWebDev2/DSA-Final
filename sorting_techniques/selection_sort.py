"""'
Select the minimum and swap it
"""

nums = [13, 46, 24, 52, 20, 9]


def selection_sort(nums: list[int]):
    for i in range(len(nums) - 1):
        min_index = i
        # find minimum
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        # swap
        nums[i], nums[min_index] = nums[min_index], nums[i]


selection_sort(nums)
print(nums)
