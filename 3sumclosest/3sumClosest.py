# https://leetcode.com/problems/3sum-closest/

# Two pointer

from typing import List

class Solution:
    def threeSumClosest(self, nums, trgt):
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l = i+1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == trgt:
                    return sum
                
                if abs(sum - trgt) < abs(ans - trgt):
                    ans = sum
                
                if sum < trgt:
                    l += 1
                elif sum > trgt:
                    r -= 1
            
        return ans

nums = [-1,2,1,-4]
target = 1
ob1 = Solution()
print(ob1.threeSumClosest(nums,target))
