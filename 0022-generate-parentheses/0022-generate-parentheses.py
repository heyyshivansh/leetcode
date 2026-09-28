class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output=[]
        open_count=0
        close_count=0
        curr=[]
        def backtrack(curr,open_count,close_count):
            if open_count==n and close_count==n:
                output.append("".join(curr))
                return
            if open_count<n:
                curr.append("(")
                backtrack(curr,open_count+1,close_count)
                curr.pop()
            if close_count<open_count:
                curr.append(")")
                backtrack(curr,open_count,close_count+1)
                curr.pop()
            return output

        return(backtrack(curr,open_count,close_count))