# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their
# start times.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# Example 3:
# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]

# Example 4:
# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]

# Example 5:
# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]

# Solution 1 -- Sorting -- Time complexity : O(nlogn) --
# Space complexity : O(logn) - Sorting takes O(logn) space or
# O(n) - Storing a copy of intervals and then sorting takes O(n) space
class Solution_1:
    def insert(intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        merge = []
        for ele in intervals:
            if not merge or merge[-1][1] < ele[0]:
                merge.append(ele)
            else:
                merge[-1][1] = max(merge[-1][1], ele[1])
        return merge
