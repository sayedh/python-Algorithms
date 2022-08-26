# https://leetcode.com/problems/integer-to-roman/

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        
        ans = ""
        for i in d:
            ans += (num//i) * d[i]
            num %= i
        return ans



num = 3
ob1 = Solution()
print(ob1.intToRoman(num))

# Explanation: 3 is represented as 3 ones.