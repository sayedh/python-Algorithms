# https://leetcode.com/problems/first-unique-character-in-a-string/




def firstUniqChar(s):
    if s == 1 : return 0 

    str = s

    while len(str) > 0 :
 
        if str[0] in str[1:]:
            str = str.replace(str[0], "")

        else :
            return s.index(str[0])

    return -1






s = "loveleetcode"
print(firstUniqChar(s))
