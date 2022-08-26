# https://leetcode.com/problems/container-with-most-water

#  Two Pointer


def maxArea(height):
    ans = 0
    l = 0
    r = len(height) - 1
    while l < r:
        if height[l] <= height[r]:
            res = height[l] * (r - l)
            l += 1
        else:
            res = height[r] * (r - l)
            r -= 1
        if res > ans: ans = res
    return ans

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))