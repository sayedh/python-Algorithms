# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# Sliding Window


def lengthOfLongestSubstring(s):
    l = 0
    ans = 0
    seen = set()
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        ans = max(ans, r-l+1)
    
    return ans


s = "abcabcbb"
print(lengthOfLongestSubstring(s))

# Explanation: The answer is "abc", with the length of 3.