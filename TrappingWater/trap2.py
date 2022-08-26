# https://leetcode.com/problems/trapping-rain-water

# Two Pointer


def trap(height):
    l = 0
    r = len(height) - 1
    lmax = height[l]
    rmax = height[r]
    ans = 0
    while l < r:
        if lmax < rmax:
            l += 1
            lmax = max(lmax, height[l])
            ans += lmax - height[l]
        else:
            r -= 1
            rmax = max(rmax, height[r])
            ans += rmax - height[r]
    return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))