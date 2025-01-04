def left_rotate_d_places(nums: list[int], d: int):
    n = len(nums)
    d = d % n

    temp = []
    for i in range(d):
        temp.append(nums[i])

    # shifting
    for i in range(d, n):
        nums[i - d] = nums[i]

    # put back temp
    for i in range(n - d, n):
        nums[i] = temp[i - (n - d)]


arr = [1, 2, 3, 4, 5, 6]
d = 7
left_rotate_d_places(arr, d)
print(arr)
