#  Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:

# Input: "aba"
# Output: True

# Example 2:

# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# Solution 1 -- Brute Force -- Time complexity : O(n^2) -- Space complexity : O(n)

# Solution 2 -- Greedy -- Time complexity : O(n) -- Space complexity : O(1)
class Solution_2:
    def validPalindrome(s):
        l, r = 0, len(s)-1

        while l < r+1:
            if s[l] != s[r]:
                one, two = s[l : r], s[l+1 : r+1]
                return one == one[::-1] or two == two[::-1]
            else:
                l += 1
                r -= 1
        return True
