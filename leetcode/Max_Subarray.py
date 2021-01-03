# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        max_sum=min(nums)
        u_sum=0
        for i in nums:
            if u_sum < 0:
                u_sum=0            
            u_sum+=i
            max_sum = max(max_sum, u_sum)    
        return max_sum    