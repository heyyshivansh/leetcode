class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
                #extract
        part1=[]
        part2=[]
        part1=(version1.split("."))
        part2=(version2.split("."))



        #           #padding 0
        # while(len(part1)!=len(part2)):
        #   if len(part1)>len(part2):
        #     part2.append("0")
        #   else:
        #     part1.append("0")
            
        #               # compare
                        

        i=0
        j=0

        while(i<len(part1) or j<len(part2)):

            num1=int(part1[i]) if i<len(part1) else 0       #alternative to padding
            num2=int(part2[j]) if j<len(part2) else 0
            

            if num1>num2:
                return 1
            elif num1<num2:
                return -1
            else:
                i+=1
                j+=1
        return 0
            

            