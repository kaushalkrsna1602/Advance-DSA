class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2 : return x
        l = 2
        r= (x//2)
        while l <= r :
            m = ((l + r)//2)
            if x == m**2:
                return m 
            elif x < m**2:
                r = m -1
            else:
                l = m + 1
        return r 
        