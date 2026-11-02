class Solution:
    def compress(self, chars: list[str]) -> int:
        s=""
        l=len(chars)
        i=0
        flag=chars[i]
        count=0
        while(i<len(chars)):
            if chars[i]==flag:
                count+=1
            
            if chars[i]!=flag:
                s+=flag
                if count>1:
                    s+=str(count)
                count=1
                flag=chars[i]
            i+=1
            
        s+=flag
        if count>1:
            s+=str(count)
        
        # print(s)
        
        i=0
        while(i<l):
            if i<len(s):
                chars[i]=s[i]
            else:
                chars.pop()
            i+=1
        return len(chars)