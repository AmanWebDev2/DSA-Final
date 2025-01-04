nums = [13, 46, 24, 52, 20, 9]
nums = [1, 2, 3, 4, 5, 6]

"""
T.C -> O(n^2)
S.C -> O(1)
"""


def bubble_sort(nums: list[int]):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(1, i + 1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


"""
T.C -> O(n^2) worst / average
T.C -> O(n) best
S.C -> O(1) 
"""


def bubble_sort_optimal(nums: list[int]):
    for i in range(len(nums) - 1, -1, -1):
        swapped = False
        for j in range(1, i + 1):
            if nums[j] < nums[j - 1]:
                swapped = True
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

        if not swapped:
            break


# bubble_sort(nums)
bubble_sort_optimal(nums)
print(nums)
