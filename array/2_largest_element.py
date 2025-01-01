arr = [2, 5, 1, 3, 0]


def brute(nums: list[int]):
    return sorted(nums)[-1]


def approach_1(nums: list[int]):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max


print(brute(arr))
print(approach_1(arr))
