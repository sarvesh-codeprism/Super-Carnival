# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Solution 1 -- Left and Right product lists -- Time complexity : O(n) -- Space complexity : O(n)
class Solution_1:
    def productExceptSelf(nums):
        length = len(nums)
        l, r, answer = [0]*length, [0]*length, [0]*length
        
        l[0], r[-1] = 1, 1
        
        for i in range(1, length):
            l[i] = l[i - 1] * nums[i - 1]
            r[length - i - 1] = r[length - i] * nums[length - i]
        
        for i in range(length):
            answer[i] = l[i] * r[i]
        
        return answer


# Solution 2 -- Only Left product list in answer -- Time complexity : O(n) -- Space complexity : O(1)
class Solution_2:
    def productExceptSelf(nums):
        length = len(nums)
        answer = [0]*length
        
        answer[0] = 1
        
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
            
        r = 1
        
        for i in range(length - 1, -1, -1):
            answer[i] = answer[i] * r
            r = r * nums[i]
            
        return answer