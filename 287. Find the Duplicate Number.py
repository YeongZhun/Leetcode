"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space."""
#Must use the slow fast pointer method, Floyd's Cycle

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #First part, find the point where slow and fast pointer meets, that is the "intersection".
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        #Second part, based on Floyd's Cycle algorithm, the distance btw the "intersection" and start of cycle is same as dist btw start of list to the start of cycle.
        #Thus, by setting another slow2 pointer, and incrementing both slow and slow2, it will reach a point where both meet
        #The point where both meet is the start of the cycle. Why do we even want to find the start of the cycle??
        #Because in a list of numbers with duplicate, when we look at it like a linked list, and have a pointer point to the next value,
        #In a linked list diagram, the duplicate number will look like a cycle, as it will have 2 pointers pointing in and out.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

#Time complexity: O(n), should be, only iterate through the list a few times 
#Space complexity: O(1), no extra memory used.            