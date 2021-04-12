# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.

# Example 1:
#   Input: s = "anagram", t = "nagaram"
#   Output: true

# Example 2:

#   Input: s = "rat", t = "car"
#   Output: false

# Solution 1 - Sorting - Time complexity : O(nlogn) -- Space complexity : O(1)
class Solution_1:
    def isAnagram(s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# Solution 2 -- Hashing(Python dictionary) -- Time complexity : O(n) --
# Space complexity : O(n)
class Solution_2:
    def isAnagram(s, t):
        letters = dict()
        if len(s) != len(t):
            return False
        else:
            for ind in range(len(s)):
                if s[ind] in letters:
                    letters[s[ind]] += 1
                else:
                    letters[s[ind]] = 1
            for ind in range(len(t)):
                if t[ind] in letters:
                    letters[t[ind]] -= 1
                elif t[ind] not in letters:
                    return False

        for val in letters.values():
            if val != 0:
                return False
        return True


# Solution_3 -- Hashing(Python module 'Counter') -- Time complexity : O(n) --
# Space complexity : O(1)
from collections import Counter


class Solution:
    def isAnagram(s, t):
        if (Counter(s) == Counter(t)):
            return True
        return False
