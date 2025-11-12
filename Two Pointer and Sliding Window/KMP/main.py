def strStr(haystack: str, needle: str) -> int:
    n = len(haystack)
    m = len(needle)
    if m == 0:
        return 0
    lps = [0] * m
    i = 0
    j = 1
    while j < m:
        if needle[i] == needle[j]:
            i += 1
            lps[j] = i
            j += 1
        else:
            if i == 0:
                lps[j] = 0
                j += 1
            else:
                i = lps[i - 1]
    i = j = 0
    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == m:
            return i - m
    return -1