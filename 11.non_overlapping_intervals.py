# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.

# Example 1:
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.

# Example 2:
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.

# Example 3:
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.

# Note:
# You may assume the interval's end point is always bigger than its start point
# Intervals like [1,2] and [2,3] have borders "touching" but they don't
# overlap each other.

# Solution 1 -- Sorting -- Time complexity : O(nlogn) --
# Space complexity : O(logn) - Sorting takes O(logn) space or
# O(n) - Storing a copy of intervals and then sorting takes O(n) space
class Solution_1:
    def eraseOverlapIntervals(intervals):
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[1])
        to_erase = 0
        max_end = intervals[0][1]
        for ind in range(1, len(intervals)):
            if intervals[ind][0] >= max_end:
                max_end = intervals[ind][1]
            else:
                to_erase += 1
        return to_erase
