# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Image --> https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Image --> https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# Solution 1 -- Reverse and Transpose -- Time complexity : O(n) - n is no. of
# cells in matrix --
# Space complexity : O(n)
class Solution_1:
    def spiralOrder(m):
        # Defining the boundaries of the matrix.
        top = 0
        bottom = len(m)-1
        left = 0
        right = len(m[0]) - 1
        res = []

        # Defining the direction in which the array is to be traversed.
        dir = 0

        while (top <= bottom and left <= right):
            if dir == 0:
                for i in range(left, right+1):  # moving left->right
                    res.append(m[top][i])

                # Since we have traversed the whole first
                # row, move down to the next row.
                top += 1
                dir = 1

            elif dir == 1:
                for i in range(top, bottom+1):  # moving top->bottom
                    res.append(m[i][right])

                # Since we have traversed the whole last
                # column, move down to the previous column.
                right -= 1
                dir = 2

            elif dir == 2:
                for i in range(right, left-1, -1):  # moving right->left
                    res.append(m[bottom][i])

                # Since we have traversed the whole last
                # row, move down to the previous row.
                bottom -= 1
                dir = 3

            elif dir == 3:
                for i in range(bottom, top-1, -1):  # moving bottom->top
                    res.append(m[i][left])
                # Since we have traversed the whole first
                # column, move down to the next column.
                left += 1
                dir = 0

        return res
