# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# The solution set must not contain duplicate subsets.
# Return the solution in any order.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Solution 1
class Solution_1:
    def subsets(nums):
        ans = [[]]
        for num in nums:
            ans += [x + [num] for x in ans]
        return ans
