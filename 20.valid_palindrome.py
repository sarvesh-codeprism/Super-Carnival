# Given a string s, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Solution 1 -- Time complexity : O(n) -- Space complexity : O(n)
class Solution_1:
    def isPalindrome(s):
        st = ''
        for ch in s:
            if ch.isalnum():
                st += ch.lower()
        return st == st[::-1]
