# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:

# Input: nums = [1]
# Output: 1

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23


# Solution 1 -- Kadane's Algorithm -- Time complexity : O(n) -- Space complexity : O(1)
class Solution_1:
    def maxSubArray(nums):
        curr_sum = 0
        max_sum = nums[0]
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum