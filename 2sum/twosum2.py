from collections import defaultdict

# Returns the indices of two numbers that add up to the target
def two_sums(nums, target):

    lookup = defaultdict(list)
    for i, num in enumerate(nums):
        needed = target - num
        if needed in lookup:
            return [lookup[needed][0], i]
        lookup[num].append(i)

    return None

print(two_sums([2,7,11,15], 17))
print(two_sums([3, 3], 6))