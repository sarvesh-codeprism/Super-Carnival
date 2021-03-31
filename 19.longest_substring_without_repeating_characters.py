# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

# Solution 1 -- Hashing -- Time complexity : O(n) -- Space complexity : O(n)
class Solution_1:
    def lengthOfLongestSubstring(s):
        l, r = 0, 0
        ans = 0
        charset = set()
        
        while r < len(s):
            if s[r] in charset:
                while s[l] != s[r]:
                    charset.remove(s[l])
                    l += 1
                l += 1
            else:
                charset.add(s[r])
                ans = max(ans, len(charset))
            r += 1
        return ans