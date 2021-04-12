# You are given an array prices where prices[i] is the price of a given stock
# on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# Example 1:
#    Input: prices = [7,1,5,3,6,4]
#    Output: 5
#    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
#    profit = 6-1 = 5.
#    Note that buying on day 2 and selling on day 1 is not allowed because
#    you must buy before you sell.

#    Example 2:
#        Input: prices = [7,6,4,3,1]
#        Output: 0
#        Explanation: In this case, no transactions are done and
#        the max profit = 0.

# Solution 1 -- Brute Force -- Time complexity:O(n^2) -- Space complexity:O(1)
class Solution_1:
    def maxProfit(prices):
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit


# Solution 2 -- One Pass -- Time complexity : O(n) -- Space complexity : O(1)
class Solution_2:
    def maxProfit(prices):
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            elif max_profit < price - min_price:
                max_profit = price - min_price
        return max_profit
