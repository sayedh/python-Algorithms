# https://leetcode.com/problems/trapping-rain-water

# Two Pointer


def trap(nums):
    ans = 0
    l = 1
    lmax = nums[l - 1]

    r = len(nums) - 2    
    rmax = nums[r + 1]

    while l <= r:
        lmax = max(lmax, nums[l])
        rmax = max(rmax, nums[r])
        if lmax < rmax:
            ans += lmax - nums[l]
            l += 1
        else:
            ans += rmax - nums[r]
            r -= 1
    return ans 



height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))