"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""
#Hint: Separate one digit out first, use for loop, then inside the loop, do 2 sum problem. 
#Sort first, to see if there are duplicates

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        #Allows us to check for duplicate easily 
        nums.sort()

        for i,a in enumerate(nums):
            #Check if current value is same as previous value, if yes means it is duplicate, not allowed, must move on to next value with 'continue'
            #Why check i > 0? So that we do not get the first value of the array, we save that as 'a', then do 2 sums on remaining values in the while loop below.
            if i > 0 and a == nums[i - 1]:
                continue
            
            left, right = 0, len(nums) - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]
                #shift right pointer to left (since it is sorted, shifting right pointer to left means the threeSum should decrease)
                if threeSum > 0:
                    right -= 1
                #shift left pointer to right (Similarly, to increase the threeSum since it is currently < 0)
                elif threeSum < 0:
                    left += 1
                else:  
                    #Do this if threeSum is = 0 
                    res.append([a, nums[left], nums[right]])
                    #update the pointer. BUT why only do for left? Do on right also can, because the while loop will check if threeSum has hit the target of 0. Will auto adjust otherwise, left -> and right <-
                    left += 1
                    #We dont want to have the same duplicate sum, so use this while loop to check, otherwise left ->
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

#Time Complexity: O(n log n) to sort the array + O(n^2) for nested loops
#Space Complexity: O(1) if we assume sorting do not take up new memory. Otherwise O(n)