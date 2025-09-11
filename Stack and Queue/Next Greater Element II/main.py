class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = [*nums, *nums]
        n = len(arr)
        stack = []
        ans = [-1]*n
        stack.append(arr[n - 1])
        for i in range(n - 2, -1, -1):
            while len(stack):
                top = stack[len(stack) - 1]
                if arr[i] < top:
                    ans[i] = top
                    break
                else:
                    stack.pop()
            stack.append(arr[i])
        return ans[0:n//2]
        


# WIthout circular

class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        stack = []
        ans = [-1]*n
        stack.append(arr[n - 1])
        for i in range((2* n) - 2, -1, -1):
            while len(stack):
                top = stack[len(stack) - 1]
                if arr[i % n] < top:
                    ans[i % n] = top
                    break
                else:
                    stack.pop()
            stack.append(arr[i % n])
        return ans[0:n]
        