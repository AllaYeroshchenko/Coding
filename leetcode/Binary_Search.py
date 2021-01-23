# 704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            center = left + (right-left)//2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center+1
            else:
                right = center-1
        return -1        