# https://leetcode.com/problems/trapping-rain-water

# Two Pointer


def trap(height):
    l = 1
    r = len(height) - 2
    lmax = height[0]
    rmax = height[-1]
    ans = 0
    while l <= r:
        lmax = max(lmax, height[l])
        rmax = max(rmax, height[r])
        if lmax < rmax:
            ans += lmax - height[l]
            l += 1
        else:
            ans += rmax - height[r]
            r -= 1
    return ans 

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))