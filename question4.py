class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        ft = 0
        st = 1
        tt = 1
        for i in range(1, n + 1):
            fot = ft + st + tt
            ft = st
            st = tt
            tt = fot
        return ft