#509 fibonacci series
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 0
        i=1
        ft=0
        st=1
        for  i in range (n):
            tt=ft+st
            ft=st
            st=tt
        return ft

