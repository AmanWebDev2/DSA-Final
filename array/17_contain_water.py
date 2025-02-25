def maxArea(height: list[int]) -> int:
    n = len(height)
    maxarea = 0
    l = 0
    r = n - 1
    while l < r:
        h = min(height[l], height[r])
        w = r - l

        vol = h * w
        maxarea = max(maxarea, vol)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return maxarea
