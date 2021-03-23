# # Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

# # Follow up:

# #     A straight forward solution using O(mn) space is probably a bad idea.
# #     A simple improvement uses O(m + n) space, but still not the best solution.
# #     Could you devise a constant space solution?

# Example 1:
# Image --> https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Image --> https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Solution 1 -- O(1) Space -- Time complexity : O(m x n) -- Space complexity : O(1)
class Solution_1:
    def setZeroes(matrix):
        m, n = len(matrix), len(matrix[0])
        row, col = set(), set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        
        for i in col:
            for j in range(m):
                matrix[j][i] = 0
        return matrix