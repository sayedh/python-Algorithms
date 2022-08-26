# https://leetcode.com/problems/container-with-most-water

#  Two Pointer

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            width = r - l
            ans = max(ans, min(height[l], height[r]) * width)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

height = [1,8,6,2,5,4,8,3,7]
ob1 = Solution()
print(ob1.maxArea(height))