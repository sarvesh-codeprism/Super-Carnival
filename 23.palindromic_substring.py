"""
Given a string, your task is to count how many palindromic substrings in this
string.

The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

"""


# Solution 1 -- BruteForce -- Time complexity: O(n^2) -- Space complexity: O(1)
class Solution_1:
    def countSubstrings(s):
        count = 0
        for ind in range(len(s)):
            for ind1 in range(ind, len(s)):
                if s[ind:ind1 + 1] == (s[ind:ind1 + 1])[::-1]:
                    count += 1
        return count
