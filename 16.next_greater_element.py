# You are given two integer arrays nums1 and nums2 both of unique elements,
# where nums1 is a subset of nums2.

# Find all the next greater numbers for nums1's elements in the corresponding
# places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to
# its right in nums2. If it does not exist, return -1 for this number.

#  Example 1:
#  Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
#  Output: [-1,3,-1]
#  Explanation:
#  For number 4 in the first array, you cannot find the next greater number for
#  it in the second array, so output -1.
#  For number 1 in the first array, the next greater number for it in the
#  second array is 3.
#  For number 2 in the first array, there is no next greater number for it in
#  the second array, so output -1.

#  Example 2:
#  Input: nums1 = [2,4], nums2 = [1,2,3,4]
#  Output: [3,-1]
#  Explanation:
#  For number 2 in the first array, the next greater number for it in the
#  second array is 3.
#  For number 4 in the first array, there is no next greater number for it in
#  the second array, so output -1.

# Solution 1 -- Hashmap and Stack
class Solution_1:
    def nextGreaterElement(nums1, nums2):
        if not nums1 or not nums2:
            return []
        map1 = {}
        stack = [nums2[0]]

        for ind in range(1, len(nums2)):
            while(stack and nums2[ind] > stack[-1]):
                map1[stack.pop()] = nums2[ind]
            stack.append(nums2[ind])

            for key in stack:
                map1[key] = -1
        return [map1[key] for key in nums1]
