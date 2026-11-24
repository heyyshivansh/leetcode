class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extract(s,i,j):
            max_st=""   
            max_l=0
            while(i>=0 and j<len(s)):
                if s[i]==s[j]:
                    if len(s[i:j+1])>max_l:
                        max_l=len(s[i:j+1])
                        max_st=s[i:j+1]
                else:
                    return max_st
                i-=1
                j+=1
            return max_st
        st1=""
        st2=""
        for x in range(len(s)):
            i=j=x
    
            m1=extract(s,i,j)
            if len(st1)<len(m1):
                st1=m1
            
            m2=extract(s,i,j+1)
            if len(st2)<len(m2):
                st2=m2

        if len(st1)>len(st2):
            return st1
        else:
            return st2
