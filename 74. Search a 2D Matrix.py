"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity."""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        #Do binary search on ROWS first, to check if target exist in any rows. 
        top, bot = 0, ROWS - 1
        #imagine going down vertically a box (matrix)
        while top <= bot:
            row = (top + bot) // 2
            #Get rightmost value with [-1] or col - 1
            #as rightmost value of each row is the biggest value, check if target is bigger or smaller than that.
            if target > matrix[row][-1]:
                top = row + 1
            #now check if target is smaller than smallest value of the current row, thus [0].
            #if smaller, then set maximum pointer (which is bot) to be row - 1 (smaller than current midpoint)
            elif target < matrix[row][0]:
                bot = row - 1
            #otherwise, it means the target belongs to this current row. break out of loop.
            else:
                break
        
        #there is a chance our top and bot condition is unrealistic, none of the condition will match, it will just exit
        #it means none of the rows contain the target value, we should return False
        if not (top <= bot):
            return False
        
        #Now we do binary search on the COLUMNS instead, AFTER finding the correct ROW above.
        #Get back the same row from above with the same formula.
        row = (top + bot) // 2
        left, right = 0, COLS - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False

#Time complexity: O(log m + log n), m and n are the rows and columns number
#Space complexity: O(1), only using pointers, no extra memory allocated