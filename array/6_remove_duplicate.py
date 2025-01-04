arr = [1, 1, 2, 2, 2, 3, 3]

"""
T.C -> O(n + n), n for creating a set and another n for converting it into list
S.C -> O(u) where u is the number of unique elements
"""


def brute(arr: list[int]):
    return list(set(arr))


def approach_1(arr: list[int]):
    unique = []  # O(n)

    # O(n)
    for num in arr:
        if len(unique) == 0 or num != unique[-1]:
            unique.append(num)

    return unique


def approach_2(arr: list[int]):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[i + 1] = arr[j]
            i += 1

    return i + 1


print(brute(arr))
print(approach_1(arr))
print(approach_2(arr))

print(arr)
