'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
class Solution:
    def maxProfit(self, prices) -> int:

            profit=0

            i,j=0,1
           
            while j< len(prices):
                    buy=prices[i]
                    sell=prices[j]
                    current_prof=sell-buy
                    if current_prof<=0:
                        i=j

                    else:
                        profit=max(profit,current_prof)
                    j+=1

            return profit
                

        