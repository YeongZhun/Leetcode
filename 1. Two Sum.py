"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
#Hint: Use Hashmaps

class Solution():
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        #HashMap solution
        prevMap = {} # number:index of number

        for index,num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], index]
                
            prevMap[num] = index
        return #not necessary since question guarantees there is a target, but just to add for completion

list_of_nums = [1,2,3,4,5,6,7,8]
test_solution = Solution()
print(test_solution.twoSum(list_of_nums,9))

#Time Complexity: O(n)
#We are iterating through the array once, and adding values to the hashmap as we go along + checking if diff value exist in hashmap.
#Space Complexity: O(n)