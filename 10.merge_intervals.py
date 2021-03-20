# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Solution 1 -- Sorting -- Time complexity : O(nlogn) -- 
#                          Space complexity : O(logn) - Sorting takes O(logn) space or 
#                                             O(n) - Storing a copy of intervals and then sorting takes O(n) space
class Solution_1:
    def merge(intervals):
        intervals.sort()
        merge = []
        for ele in intervals:
            if not merge or merge[-1][1] < ele[0]:
                merge.append(ele)
            else:
                merge[-1][1] = max(merge[-1][1], ele[1])
        return merge
                