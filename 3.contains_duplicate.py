# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

#    Input: nums = [1,2,3,1]
#    Output: true


# Example 2:

#    Input: nums = [1,2,3,4]
#    Output: false

# Example 3:
    
#    Input: nums = [1,1,1,3,3,4,3,2,4,2]
#    Output: true

# Solution 1 -- Linear Search -- Time complexity : O(n^2) -- Space complexity : O(1)
class Solution_1:
    def containsDuplicate(nums):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False

# Solution 2 -- Sorting -- Time complexity : O(nlogn) -- Space complexity : O(1)
class Solution_2:
    def containsDuplicate(nums):
        nums.sort()
        for ind in range(len(nums) - 1):
            if nums[ind] == nums[ind + 1]:
                return True
        return False

# Solution 3 -- Hashing -- Time complexity : O(n) -- Space complexity : O(n)
class Solution_3:
    def containsDuplicate(nums):
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False
