# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dsave={}
        count=0
        for num in nums:
            diff=target-num
            if diff in dsave:
                return [count, dsave[diff]]
            dsave[num]=count
            count+=1
            