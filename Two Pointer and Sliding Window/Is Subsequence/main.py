def isSubsequence(s, t):
    i = j = 0
    while j < len(t):
        if s[i] == t[j]:
            i = i + 1
        j += 1
    return i == len(s)

print(isSubsequence("abc", "ahbgdc"))