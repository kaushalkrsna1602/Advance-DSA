def is_hash_same(a, b):
    return a == b


def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    hashS = [0] * 26
    hashW = [0] * 26
    window_length = len(s1)
    for i in range(window_length):
        hashS[ord(s1[i]) - ord("a")] += 1
        hashW[ord(s2[i]) - ord("a")] += 1
    i = 0
    j = window_length - 1
    while j < len(s2):
        if is_hash_same(hashS, hashW):
            return True
        hashW[ord(s2[i]) - ord("a")] -= 1
        i += 1
        j += 1
        if j < len(s2):
            hashW[ord(s2[j]) - ord("a")] += 1
    return False
