from collections import defaultdict

"""
T.C -> O(n*klog(k))
S.C -> O(n*k)
"""


def group_anagram(strs: list[str]):
    mpp = defaultdict(list)
    for s in strs:
        mpp[tuple(sorted(s))].append(s)
    return list(mpp.values())


"""
T.C -> O(n*k)
S.C -> O(n*k)
"""


def group_anagram2(strs: list[str]):
    mpp = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        mpp[tuple(count)].append(s)
    return list(mpp.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram(strs))
print(group_anagram2(strs))
