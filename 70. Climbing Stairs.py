"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""
#Hint: This is a recursion or DP problem.
#e.g. if n = 4, you have to first find all n = 3, n = 2, n = 1 number of steps first. So there is a pattern to recurse to, and we need to define the base cases. 
#n = 1 means 1 step only. n = 2 means 1 + 1 or 2. 

#Recursion
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Base cases
        if n == 0:
            return(0)
        
        if n == 1:
            return(1)

        if n == 2:
            return(2)
        
        #e.g 
        #n(3) = n(2) + n(1)
        #n(4) = n(3) + n(2) ...

        return(self.climbStairs(n-1) + self.climbStairs(n-2))

test_solution = Solution()
print(test_solution.climbStairs(5))