arr = [1, 2, 4, 7, 7, 5]


def brute(nums: list[int]):
    nums_sorted = sorted(nums)
    max = nums_sorted[-1]
    second_max = -1
    n = len(nums)
    for i in range(n - 2, -1, -1):
        if nums_sorted[i] != max:
            second_max = nums_sorted[i]
            break
    return second_max


def approach_1(nums: list[int]):
    largest = nums[0]
    second_largest = -1
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


print(brute(arr))
print(approach_1(arr))
