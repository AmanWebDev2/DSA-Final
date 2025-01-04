def insertion_sort(nums: list[int]):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1


nums = [6, 8, 9, 12, 14, 15, 5]
insertion_sort(nums)
print(nums)
