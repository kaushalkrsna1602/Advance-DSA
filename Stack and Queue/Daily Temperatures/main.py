class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack = []
        n = len(arr)
        ans = [0] * n
        stack.append(n-1)
        for i in range(n-2, -1, -1):
            while len(stack):
                top = stack[len(stack) - 1]
                if arr[i] >= arr[top]:
                    stack.pop()
                else :
                    ans[i] = top - i
                    break
            stack.append(i)
        return ans        