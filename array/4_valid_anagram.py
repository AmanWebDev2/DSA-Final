s = "anagram"
t = "nagaram"


"""
T.C -> O(nlogn)
S.C -> O(1)
"""


def brute(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


"""
T.C -> O(n + m)
S.C -> O(26) === O(1)
"""


def approach_hashing(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash = [0] * 26  # constant space O(26)

    # O(n)
    for char in s:
        hash[ord(char) - ord("a")] += 1

    # O(m)
    for char in t:
        hash[ord(char) - ord("a")] -= 1

    # O(26)
    for num in hash:
        if num != 0:
            return False

    return True


"""
T.C -> O(n)
S.C -> O(n)
"""

from collections import defaultdict


def approach_map(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    mpp = defaultdict(int)

    for char in s:
        mpp[char] += 1

    for char in t:
        mpp[char] -= 1

    for value in mpp.values():
        if value != 0:
            return False

    return True


print(brute(s, t))
print(approach_hashing(s, t))
print(approach_map(s, t))
