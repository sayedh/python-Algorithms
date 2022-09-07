# https://leetcode.com/problems/container-with-most-water

#  Two Pointer


def maxArea(nums):
    ans = 0
    l = 0
    r = len(nums) - 1
    while l < r:
        w = r - l
        h = min(nums[l], nums[r])
        ans = max(ans, h * w)
        
        if nums[l] <= nums[r]:
            l += 1
        else:
            r -= 1
    return ans

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))