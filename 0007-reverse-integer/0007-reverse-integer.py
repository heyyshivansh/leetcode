class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x<0:
            sign=-1
        else:
            sign=1
        x*=sign
        length = len(str(abs(x)))
        for i in range(length):
            digit=x%10
            rev=(rev*10)+digit
            x//=10

        rev*=sign
        
        if rev<(-2)**31 or rev>((2)**31 -1):
            return 0
        return rev

