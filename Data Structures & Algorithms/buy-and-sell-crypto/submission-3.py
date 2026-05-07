class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        max_profit = 0
        for price in prices:
            curr_min = min(curr_min, price)
            max_profit = max(max_profit, price - curr_min)
        return max_profit



























        # max_profit = 0
        # for price in prices[1:]:
        #     curr_min = min(curr_min, price)
        #     max_profit = max(max_profit, price-curr_min)
        # return max_profit