class Solution(object):
    def isHappy(self, n):
        seen=set()
        def square(n):
            sq=0
            while(n>0):
                digit=n%10
                sq+=(digit*digit)
                n=n//10
            return sq

        def func(n):
            if n==1:
                return True
            if n in seen:
                return False
            seen.add(n)
            next_num=square(n)
            return func(next_num)

        return(func(n))

