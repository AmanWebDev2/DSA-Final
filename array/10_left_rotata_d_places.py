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
d = 4
# left_rotate_d_places(arr, d)
# print(arr)

"""
    T.C -> O(d) + O(n-d) + O(n) => O(2n) => O(n)
    S.C -> O(1)
"""


def left_rotate_d_places2(nums: list[int], d: int):
    n = len(nums)
    d = d % n
    sort(nums, 0, d - 1)
    sort(nums, d, n - 1)
    sort(nums, 0, n - 1)


def sort(nums: list[int], i: int, j: int):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


left_rotate_d_places2(arr, d)
print(arr)
