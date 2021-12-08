# https://www.youtube.com/watch?v=1pkOgXD63yU&ab_channel=NeetCode
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# One pass soultion using 2 pointers/sliding window method, is O(N) time and O(1) memory

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left and right pointers for buy and sell date (have to buy low and sell high)
        #the buy date needs to be < than the sell date
        buy = 0
        sell = 1
        maxProfit = 0
        #go through the list
        while sell < len(prices):
            #if this is a profit
            if prices[buy] <= prices[sell]:
                #see if its > than the maxProfit and update it
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                #if not shift the left pointer to the sell date, and go from there
                #if buy > sell its not a profit so try again and start buying at the previous sell date
                buy = sell
            #either way sell is incremented and keeps going until the end
            sell += 1
        return maxProfit
