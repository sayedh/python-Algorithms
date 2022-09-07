# https://leetcode.com/problems/two-sum/

# Brute Force

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] + nums[i] == target:
                return [i, j]



nums = [int(x) for x in input("  array: ").split()]
target = int(input(" target: "))

print("indices:", twoSum(nums, target))

