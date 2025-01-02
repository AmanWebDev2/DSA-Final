arr = [1, 2, 2, 3, 3, 4]
arr2 = [1, 2, 1, 3, 4]


def is_sorted(arr: list[int]) -> bool:
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


print(is_sorted(arr))
print(is_sorted(arr2))
