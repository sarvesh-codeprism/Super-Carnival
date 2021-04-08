"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Example 1:
Image link -> https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""


# Solution 1
class Solution_1:
    def trap(height):
        if height == []:
            return 0
        left = [0]*len(height)
        right = [0]*len(height)
        max_r = height[-1]
        max_l = height[0]
        for ind in range(len(height)):
            if height[ind] >= max_l:
                max_l = height[ind]
            left[ind] = max_l
            if height[len(height) - ind - 1] >= max_r:
                max_r = height[len(height) - ind - 1]
            right[len(height) - ind - 1] = max_r

        return sum([min(left[i], right[i])-height[i] for i in range(len(height))])
