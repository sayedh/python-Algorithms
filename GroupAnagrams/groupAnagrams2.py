# https://leetcode.com/problems/group-anagrams/


def groupAnagrams(strs):
    ans = []
    d = {}
    for i in strs:
        sortWord = tuple(sorted(i))
        if sortWord in d:
            d[sortWord].append(i)
        else:
            d[sortWord] = [i]
        
    for i in d.values():
        ans.append(i)
    return ans






strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))