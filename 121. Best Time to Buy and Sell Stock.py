"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
#Hint: Use 2 pointers, left and right at the start. Compare left and right. We have to make sure left is as low as possible, right is as high as possible, to get highest profit.

class Solution():
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1
        maxP = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                #This is to compare and get the max value of current max profit vs current profit, and let the highest be the new maxP variable, each iteration.
                maxP = max(maxP, profit)
            else:
                #Set left to be the current right position, since right pointer is lower than left pointer, and we need left pointer to be as low as possible.
                left = right
            right += 1
        return maxP

test_solution = Solution()
price_list = [7,1,5,4,6,2,1,10]
print(test_solution.maxProfit(price_list))

#Time Complexity: O(n) , we only need to go through the list once
#Space Complexity: O(1) , we use 2 pointers technique (sliding window), only moving the pointers, didnt create any extra arrays.