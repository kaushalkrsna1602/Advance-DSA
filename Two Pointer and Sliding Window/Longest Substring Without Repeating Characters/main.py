def lengthOfLongestSubstring(s: str) -> int:
    map = {}
    maxWS = 0
    i = 0
    for j in range(len(s)):
        if s[j] in map and map[s[j]] >= i:
            i = map[s[j]] + 1
        map[s[j]] = j
        currWS = j - i + 1
        maxWS = max(maxWS, currWS)
    return maxWS