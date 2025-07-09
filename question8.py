#remaning
#1137. N-th Tribonacci Number
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            ft=0
            st=1
            tt=1
            i=1
            for i in range(n):
                fort=ft+st+tt
                ft,st,tt=st,tt,fort
            return ft