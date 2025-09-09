class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngeMap = {}
        stack = []
        n = len(nums2)
        stack.append(nums2[n - 1])
        ngeMap[nums2[n - 1]] = -1
        for i in range(n - 2, -1, -1):
            while len(stack):
                if stack[len(stack) - 1] < nums2[i]:
                    stack.pop()
                else:
                    ngeMap[nums2[i]] = stack[len(stack) - 1]
                    break
            if len(stack) == 0:
                ngeMap[nums2[i]] = -1
            stack.append(nums2[i])
        return [ngeMap[x] for x in nums1]