# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        left, currmax = [], 0
        for h in height:
            currmax = max(currmax, h)
            left.append(currmax-h)
            
        right, currmax = [], 0
        for h in height[::-1]:
            currmax = max(currmax, h)
            right.append(currmax-h)
            
        return sum([min(l, r) for l, r in zip(left, right[::-1])])    