# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range (len(nums)) :
            i1, i2 = i+1, len(nums)-1
            while i1<i2:
                currentSum = nums[i]+nums[i1]+nums[i2]
                if currentSum == 0:
                    if [nums[i], nums[i1], nums[i2]] not in result:
                        result.append([nums[i], nums[i1], nums[i2]])        
                if currentSum>=0:
                    i2-=1
                else:
                    i1+=1
        return result

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positive=sorted([x for x in nums if x >= 0], reverse=True)
        negative=sorted([x for x in nums if x < 0])
        set_pos = set(positive)
        set_neg = set(negative)
        if len(positive) == 0:
            return []
        if len(positive) == positive.count(0) and len(positive)>2:
            return [[0, 0, 0]]
        #print(positive)
        #print(negative)
        result=[]
        if positive.count(0)>2:
            result.append([0, 0, 0])
        for i in range(len(positive)):
            for j in range(i+1, len(positive)):
                if -(positive[i]+positive[j]) in set_neg:
                    if [positive[i], positive[j], -(positive[i]+positive[j])] not in result:
                        result.append([positive[i], positive[j], -(positive[i]+positive[j])])
                                           
        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                if -(negative[i]+negative[j]) in set_pos:
                    if [negative[i], negative[j], -(negative[i]+negative[j])] not in result:
                        result.append([negative[i], negative[j], -(negative[i]+negative[j])])
                    
        return result               
"""        