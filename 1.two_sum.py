# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly 'one solution', and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Solution 1 -- Time complexity : O(n^2) -- Space complexity : O(1)
class Solution_1:
    def twoSum(nums, target):
        sol = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    sol += [i, j]
        return sol
    
# Solution 2 -- Time complexity : O(n) -- Space complexity : O(n)
class Solution_2:
    def twoSum(nums, target):
        sums = {}
        for ind in range(len(nums)):
            if (target - nums[ind]) in sums:
                return [sums[target-nums[ind]], ind]
            else:
                sums[nums[ind]] = ind