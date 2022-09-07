# https://leetcode.com/problems/group-anagrams/


def groupAnagrams(strs):
    ans = []
    d = {}
    for i in strs:
        sort = tuple(sorted(i))
        if sort in d:
            d[sort].append(i)
            print(d)
        else:
            d[sort] = [i]
        
    for i in d.values():
        ans.append(i)
    return ans






strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))