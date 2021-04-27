#!/usr/bin/env python3

# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Solution 1
class Solution_1:
    def subsetsWithDup(nums):
        ans = [[]]
        for num in sorted(nums):
            ans += [x + [num] for x in ans if x+[num] not in ans]
        return ans
