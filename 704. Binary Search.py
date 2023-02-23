"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        max_point = len(nums) - 1
        min_point = 0
        
        while min_point <= max_point:
            #OR mid_point = min_point + ((max_point - min_point) //2) <-- Alternate way IF tested on stack overflow, as max_point+min_point could overflow if integer given is ultra large
            mid_point = (max_point+min_point)//2

            if nums[mid_point] > target:
                max_point = mid_point - 1

            elif nums[mid_point] < target:
                min_point = mid_point + 1

            else:
                #if mid_point not < or > than target, means it IS the target. 
                return mid_point
        #if while loop finishes, min_point >= max_point already still cannot find, then the target does not exist in this list, return -1 as per question.
        return -1

test_solution = Solution()
nums = [1,2,3,4,5,6,7,8,9,10]
target = 2
print(test_solution.search(nums,target))

#Time Complexity: O(log n) as per requirement. Because it cuts half of the array each time.
#Space Complexity: O(1) , it is just 2 pointers/variables moving, no new data created.