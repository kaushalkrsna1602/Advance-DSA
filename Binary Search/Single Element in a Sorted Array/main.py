class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = l + ((r-l)//2)
            if arr[m] == arr[m - 1]:
                leftCount = m -1 -l
                if leftCount % 2 == 1:
                    r = m - 1
                else :
                    l = m + 1
            elif arr[m] == arr[m+1]:
                leftCount = m - l
                if leftCount % 2 == 1:
                    r = m - 1
                else:
                    l = m + 2
            else:
                return arr[m]