# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# Sliding Window


def lengthOfLongestSubstring(s):
    i = 0
    j = 0
    ans = 0
    seen = set()
    while i<len(s) and j<len(s):
        if s[j] not in seen:
            seen.add(s[j])
            ans=max(ans,int(len(seen)))
            j+=1
        else:
            seen.remove(s[i])
            i+=1
    return ans


s = "abcabcbb"
print(lengthOfLongestSubstring(s))

# Explanation: The answer is "abc", with the length of 3.