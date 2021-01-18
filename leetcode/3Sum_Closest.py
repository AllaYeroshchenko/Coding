# 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        import sys
        closestSum = sys.maxsize
        nums.sort()
        for i in range (len(nums)) :
            i1, i2 = i+1, len(nums)-1
            while i1<i2:
                currentSum = nums[i]+nums[i1]+nums[i2]
                if abs(target-currentSum)<abs(target-closestSum):
                    closestSum=currentSum
                if currentSum>target:
                    i2-=1
                else:
                    i1+=1
        return closestSum