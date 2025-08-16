class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]
            else:
                removals += 1
                prev_end = min(prev_end, intervals[i][1])

        return removals
