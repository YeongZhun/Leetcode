"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""
#Hint: Use two pointers at start and end. 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Using two pointers 
        left, right = 0, len(height) - 1
        #create max area as 0 first, update as we iterate
        max_area = 0

        while left < right:
            #General formula to determine the largest container possible
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, curr_area)

            #If left value < right value, we need to shift left to -> , otherwise shift right to <-
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

#Time Complexity: O(n) , we only iterate through the array at most once
#Space Complexity: O(1) , using pointers, we did not create new memory