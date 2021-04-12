# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.

# Example 1:
# Image --> https://assets.leetcode.com/uploads/2020/11/04/word2.jpg
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
# word = "ABCCED"
# Output: true

# Example 2:
# Image --> https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
# word = "SEE"
# Output: true

# Example 3:
# Image --> https://assets.leetcode.com/uploads/2020/10/15/word3.jpg
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
# word = "ABCB"
# Output: false

class Solution_1:
    def exist(self, board, word):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0] and \
                   self.search(board, y, x, 0, word):
                    return True
        return False

    def search(self, board, y, x, ind, word):
        if ind == len(word):
            return True
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[y]) or \
           board[y][x] != word[ind]:
            return False

        temp = board[y][x]
        board[y][x] = ' '
        found = self.search(board, y + 1, x, ind + 1, word) or \
            self.search(board, y - 1, x, ind + 1, word) or \
            self.search(board, y, x + 1, ind + 1, word) or \
            self.search(board, y, x - 1, ind + 1, word)

        board[y][x] = temp
        return found
