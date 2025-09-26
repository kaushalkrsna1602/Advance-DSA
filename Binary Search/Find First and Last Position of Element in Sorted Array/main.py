# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 
from typing import List

class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        ans = [-1, -1]

        # Find leftmost index (lower bound)
        l, r = 0, len(arr) - 1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] < target:
                l = m + 1
            else:
                r = m
        if len(arr) > 0 and arr[l] == target:
            ans[0] = l
        else:
            return ans  # target not found, return early

        # Find rightmost index (upper bound)
        l, r = 0, len(arr) - 1
        while l < r:
            m = l + (r - l + 1) // 2  # upper mid
            if arr[m] > target:
                r = m - 1
            else:
                l = m
        ans[1] = l

        return ans
