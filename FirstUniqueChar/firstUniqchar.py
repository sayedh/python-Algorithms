# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == 1 : return 0 

        s1 = s

        while len(s1) > 0 :
            if s1[0] in s1[1:] :
                s1 = s1.replace(s1[0] , "")
            else :
                return s.index(s1[0])

        return -1


s = "loveleetcode"
ob1 = Solution()
print(ob1.firstUniqChar(s))
