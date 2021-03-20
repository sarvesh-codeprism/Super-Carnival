# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:

# Input: nums = []
# Output: []

# Example 3:

# Input: nums = [0]
# Output: []

# Solution 1 -- Two Pointer -- Time complexity : O(n^2) -- Space complexity : O(n)
class Solution_1:
    def threeSum(nums):
        n = len(nums)
        if n < 3: return []
        result = []
        nums.sort()
        for i in range(n-2):
            if i == 0 or nums[i] != nums[i-1]:
                j,k = i+1, n-1
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]: j += 1
                        while j < k and nums[k] == nums[k-1]: k -= 1
                        j, k = j+1, k-1
                    elif sum < 0: j += 1
                    else: k -= 1
        return result