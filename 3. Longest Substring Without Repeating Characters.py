"""Given a string s, find the length of the longest 
substring without repeating characters."""
#Hint: Use set, and 2 pointers left and right starting at the beginning


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        left = 0 
        res = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remoe(s[left])
                left += 1
            charSet.add(s[right])
            #size of current substring, + 1 because we count from 0 (right?)
            res = max(res, right - left + 1)
        return res