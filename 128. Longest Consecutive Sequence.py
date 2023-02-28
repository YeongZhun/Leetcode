"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""

#Hint: iterate through initial array, use set to check if values have [index - 1] left neighbors
#If no, that means they are the start of the first sequence. Then start checking if [index + 1] is value + 1, and count

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for n in nums:
            #check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

#Time complexity: O(n), n is size of array
#Space complexity: O(n)