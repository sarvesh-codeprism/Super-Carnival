# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Solution 1 -- Stack -- Time complexity : O(n) -- Space complexity : O(n)
class Solution_1:
    def isValid(s):
        arr = []
        braces = {'{': '}', '[': ']', '(': ')'}

        for char in s:
            if char in braces:
                arr.append(char)
            elif len(arr) != 0 and char == braces[arr[-1]]:
                arr.pop()
            else:
                return False

        return len(arr) == 0
