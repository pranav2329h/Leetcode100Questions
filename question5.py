#1518. Water Bottles
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans=numBottles
        while numBottles>=numExchange:
            newBottles=numBottles // numExchange
            remBottles=numBottles % numExchange
            ans+=newBottles
            numBottles=newBottles+remBottles
        return ans