# 1614. Maximum Nesting Depth of the Parentheses


class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxd=0
        for syb in s:
            if syb=="(":
                count+=1
            if syb==")":
                count-=1
            if count>maxd:
                maxd=count
        return maxd        
                
            
        