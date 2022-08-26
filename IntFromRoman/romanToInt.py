# https://leetcode.com/problems/roman-to-integer/

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        l = 0
        
        for i in s[::-1]:    
            if d[i] >= l:
                ans += d[i]    
            else:
                ans -= d[i]     
            l = d[i]
        return ans


s = "III"
ob1 = Solution()
print(ob1.romanToInt(s))

# Input: s = "III"
# Output: 3
# Explanation: III = 3.