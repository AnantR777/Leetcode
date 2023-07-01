class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open,close,ans=0,0,0
        for i in s: # l to r traversal
            if i=="(":
                open+=1
            else:
                close+=1
            if close==open:
                ans=max(ans,close+open) # compares to current max substring
            elif close>open:
                open, close = 0, 0 # number of open brackets must be geq number of closed
        open, close = 0, 0
        # r to l traversal
        for i in range(len(s)-1,-1,-1): # start is inclusive, stop is not
            if s[i] == "(":
                open+=1
            else:
                close+=1
            if close==open:
                ans=max(ans,close+open)
            elif open>close:
                open, close = 0, 0
        return ans
