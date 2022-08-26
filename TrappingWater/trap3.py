# https://leetcode.com/problems/trapping-rain-water

# Two Pointer


def trap(height):
    l = 0
    r = len(height) - 1
    lmax = 0
    rmax = 0
    ans = 0
    while l < r:
        if height[l] <= height[r]:
            if height[l] <= lmax :
                ans += lmax-height[l]
                l+=1
            else :
                lmax = height[l]
                l+=1
        else :
            if height[r] <= rmax :
                ans += rmax-height[r]
                r-=1
            else :
                rmax = height[r]
                r-=1
    return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))