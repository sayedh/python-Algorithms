nums = [2,7,11,15]
output = []
k = 9

for elem in nums:
    p = k - elem
    if p in nums:
        output.append(p)
        output.append(elem)
        break
print(output)