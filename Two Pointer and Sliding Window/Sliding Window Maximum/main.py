from collections import deque

class Solution:
    def maxSlidingWindow(self, arr, k):
        res = []
        q = deque()

        i = j = 0
        while j < len(arr):
            while q and arr[j] > q[-1]:
                q.pop()
            q.append(arr[j])

            if j >= k - 1:
                res.append(q[0])
                if arr[i] == q[0]:
                    q.popleft()
                i += 1
            j += 1

        return res
