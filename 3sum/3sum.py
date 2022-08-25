# https://leetcode.com/problems/3sum/

# Two pointer

from typing import List

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]: continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return res

nums = [-1, 0, 1, 2, -1, -4]
ob1 = Solution()
print(ob1.threeSum(nums))
