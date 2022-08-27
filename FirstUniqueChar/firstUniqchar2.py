# https://leetcode.com/problems/first-unique-character-in-a-string/




def firstUniqChar(s):
    d = {}
    seen = set()
    for i, c in enumerate(s):
        if c not in seen:
            d[c] = i
            seen.add(c)
        elif c in d:
            del d[c]
    return min(d.values()) if d else -1



s = "loveleetcode"
print(firstUniqChar(s))
