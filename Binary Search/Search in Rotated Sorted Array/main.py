class Solution:
    def search(self, arr, target: int) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target == arr[m]:
                return m
            if arr[l] <= arr[m]:
                if target < arr[m] and target >= arr[l]:
                    r = m - 1
                else:
                    l = m + 1
            else: 
                if target > arr[m] and target <= arr[r]:
                    l = m + 1
                else:
                    r = m - 1
        return - 1