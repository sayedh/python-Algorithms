# https://leetcode.com/problems/3sum/

# Two pointer


def threeSum(nums):
    nums.sort()
    ans = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i - 1] == nums[i]: continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                ans.append((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif sum < 0:
                l += 1
            else:
                r -= 1
    return ans

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
