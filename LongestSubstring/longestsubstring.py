# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
ob1 = Solution()
print(ob1.lengthOfLongestSubstring(s))

# Explanation: The answer is "abc", with the length of 3.