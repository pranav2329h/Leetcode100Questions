#989. Add to Array-Form of Integer
from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []
        p = len(num) - 1
        carry = 0
        while p >= 0 or k > 0:
            numval = 0
            if p >= 0:
                numval = num[p]
            d = k % 10
            sum_value = numval + d + carry
            digit = sum_value % 10
            carry = sum_value // 10
            ans.append(digit)
            p -= 1  # moving the pointer
            k //= 10  # removing the last digit from k
        if carry > 0:
            ans.append(carry)  # adding carry to the list
        ans.reverse()  # reversing the ans list
        return ans