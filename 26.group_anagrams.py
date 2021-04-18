#!/usr/bin/env python3

# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Solution 1 -- Time complexity : O(n) -- Space complexity : O(n)
class Solution_1:
    def groupAnagrams(strs):
        result = dict()
        for st in strs:
            sorted_str = "".join(sorted(st))
            if sorted_str in result:
                result[sorted_str] += [st]
            else:
                result[sorted_str] = [st]
        return result.values()
