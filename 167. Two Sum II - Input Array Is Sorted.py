"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
#Hint: 2 pointers

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            curSum = numbers[left] + numbers[right]
            
            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                # add +1 because of question requirement to have non-zero counting
                return [left+1, right+1]
        return []

#Time Complexity: O(n) , go through list at most once only
#Space Complexity: O(1) , only using pointers, no extra memory allocated