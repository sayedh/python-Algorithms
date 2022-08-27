# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for i in strs:
            sort = tuple(sorted(i))
            if sort in d:
                d[sort].append(i)
            else:
                d[sort] = [i]
            
        for i in d.values():
            ans.append(i)
        return ans








strs = ["eat","tea","tan","ate","nat","bat"]
ob1 = Solution()
print(ob1.groupAnagrams(strs))