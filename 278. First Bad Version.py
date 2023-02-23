"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""
#Hint: Binary Search. 
#First target search midpoint, if API bool is False (means it is a good ver), means every other value lower than midpoint is GOOD. Let midpoint be the minimum now, and repeat.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return

class Solution(object):
    def firstBadVersion(self, n:int) -> int:
        #n is total number of versions. e.g. n = 10, and bad version = 5. This function will output 5 (integer)
        #Set answer to -1 initially (in case results all bad), update it as we move along
        answer = -1

        if n == 1:
            return 1

        min_point = 1
        max_point = n
        while min_point < max_point:
            #one way to find mid_point
            #mid_point = (1+n)//2
            #Alternate better way of finding mid_point:
            mid_point = min_point + ((max_point-min_point)//2)
            if isBadVersion(mid_point):
                max_point = mid_point - 1
                answer = mid_point
            else:
                min_point = min_point + 1
        return answer
