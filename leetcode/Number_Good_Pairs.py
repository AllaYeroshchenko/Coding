# 1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        checked={x: nums.count(x) for x in nums}
        ct=0
        for val in checked.values():
            if val > 1:
                #ct += val**2//2-val//2
                ct += sum(range(1, val))
        return ct         
