class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp=x
        rev=0
        for i in range(len(str(abs(x)))):
            digit=temp%10
            rev=(rev*10)+digit
            temp//=10
        
        return rev==x