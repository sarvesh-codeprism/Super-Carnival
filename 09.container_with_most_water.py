# # Given n non-negative integers a1, a2, ..., an , where each represents
# # a point at coordinate (i, ai). n vertical lines are drawn such that the
# # two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which
# # together with the x-axis forms a container, such that the container
# contains the most water.

# # Notice that you may not slant the container.

# Example 1:
# Link to image
# --> https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by
# array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can
# contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16

# Example 4:
# Input: height = [1,2,1]
# Output: 2

# Solution 1 - Brute Force - Time complexity:O(n^2) -- Space complexity:O(1)
# Approach : Fix two pointers for first two line and use two for loops to
# iterate
#            Store and update maximum value, after the completion of loops
#            return the value

# Solution 2 -- Two Pointers One Pass -- Time complexity : O(n) --
# Space complexity : O(1)
class Solution_2:
    def maxArea(height):
        maximum = 0
        left, right = 0, len(height) - 1
        while left < right:
            left_h, right_h = height[left], height[right]
            min_h = min(left_h, right_h)
            maximum = max(min_h*(right-left), maximum)
            if left_h < right_h:
                left += 1
            else:
                right -= 1
        return maximum
