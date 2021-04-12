# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Example 3:
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Example 4:
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000

# Example 5:
# Input: nums1 = [2], nums2 = []
# Output: 2.00000

# Solution 1 - Sorting - Time complexity : O(nlogn) -- Space complexity : O(n)
class Solution_1:
    def findMedianSortedArrays(nums1, nums2):
        for num in nums2:
            nums1.append(num)

        nums1.sort()

        k = len(nums1)

        if k % 2 == 0:
            return (nums1[k//2] + nums1[(k//2) - 1]) / 2
        else:
            return nums1[k//2]
