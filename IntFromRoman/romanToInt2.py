# https://leetcode.com/problems/roman-to-integer/

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


def romanToInt(s):
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = d.get(s[-1])

    
    for i in reversed(range(len(s) - 1)):
        if d[s[i]] < d[s[i + 1]]:
            ans -= d[s[i]]
        else:
            ans += d[s[i]]
    return ans




s = "III"
print(romanToInt(s))

# Input: s = "III"
# Output: 3
# Explanation: III = 3.