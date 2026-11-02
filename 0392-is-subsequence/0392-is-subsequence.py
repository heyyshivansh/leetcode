class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        if len(s)==0:
            return True
        while i<len(t) and j<len(s):
            if t[i]==s[j]:
                i+=1
                j+=1
                if j==len(s):
                    return True
                
        
            if i==len(t) and j!=len(s):
                return False
            if i==len(t) and j==len(s):
                return True
                break
            
            if t[i]!=s[j]:
                i+=1
        
        return False