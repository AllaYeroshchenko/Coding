# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        intervals.sort(key = lambda x:x[0])
        if len(intervals)<=1:
            return intervals
        i=1
        while i<=len(intervals):
            if i == len(intervals):
                merged_intervals.append(intervals[i-1])
                return merged_intervals
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i] = [min(intervals[i-1][0], intervals[i][0]), max(intervals[i][1], intervals[i-1][1])]
                i+=1
            else:
                merged_intervals.append(intervals[i-1])
                i+=1

                