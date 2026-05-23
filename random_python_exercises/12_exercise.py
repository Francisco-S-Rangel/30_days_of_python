def strStr(haystack: str, needle: str) -> int:
    if needle == "": return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            for j in range(len(needle)):
                if haystack[j + i] != needle[j]:
                    break
                if j == len(needle) -1:
                    return i
    
    return -1

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode","leeto"))
print(strStr("mississippi","issipi"))