class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x % 10 == 0 and x != 0):
            return False
        n=x
        revNum=0
        d=0
        while n>0:
            d=n%10
            revNum=revNum*10+d
            n=n//10
        if revNum==x:
            return True
        else:
            False
