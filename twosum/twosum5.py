
def twoSum(nums, target):
   """
   :type nums: List[int]
   :type target: int
   :rtype: List[int]
   """
   required = {}
   for i in range(len(nums)):
      if target - nums[i] in required:
         return [required[target - nums[i]],i]
      else:
         required[nums[i]]=i


input_list = [2,8,12,15]
print(twoSum(input_list, 20))



