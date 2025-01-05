def top_k(nums: list[int], k: int):
    mpp = {}
    for num in nums:
        mpp[num] = 1 + mpp.get(num, 0)

    mpp_sorted = dict(sorted(mpp.items(), key=lambda item: item[1], reverse=True))
    print(mpp_sorted)
    res = []
    i = 1
    for val in mpp_sorted.keys():
        if i > k:
            break
        res.append(val)
        i += 1
    return res


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(top_k(nums, k))

import heapq


def top_k_heap(nums: list[int], k: int):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # default min heap
    # insert (freq,val) so that it maintains heap on the basis of freq
    heap = []
    for num in count.keys():
        heapq.heappush(heap, (count[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res


print(top_k_heap(nums, k))
