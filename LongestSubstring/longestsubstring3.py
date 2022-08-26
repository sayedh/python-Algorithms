# https://leetcode.com/problems/longest-substring-without-repeating-characters/




def lengthOfLongestSubstring(s):
    seen = {}
    l = 0
    ans = 0
    for r in range(len(s)):

        if s[r] not in seen:
            ans = max(ans,r-l+1)
        else:
            if seen[s[r]] < l:
                ans = max(ans,r-l+1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return ans

s = "abcabcbb"
print(lengthOfLongestSubstring(s))

# Explanation: The answer is "abc", with the length of 3.