"""You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0

        left = 0 
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)

            #make sure current window is valid, and check number of replacements needed to make for string to be longest
            #make sure the number of replacement is less than k, otherwise shift the pointer
            #e.g. A,B,B,A,B <-- 2A and 3B. That would be 5 (size of window) - 3 (max count, 3B) = 2.
            #Meaning if k = 2, we are allowed to change 2 As to 2Bs, and make the total string have 5 Bs.
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            #update max of result, (right-left+1) is size of current window
            res = max(res, right - left + 1)

#Time complexity: O(n), technically 26*n, possibel to scan through every alphabet.