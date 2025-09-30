from typing import List

class Solution:
    def findMin(self, a: List[int]) -> int:
        l, r = 0, len(a) - 1
        while l < r:
            m = l + (r - l) // 2
            if a[m] > a[r]:
                # Minimum is in the right half
                l = m + 1
            else:
                # Minimum is in the left half (including m)
                r = m
        return a[l]
