class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        ill check if 1 > 7 
        ill get min of 1,7 and difference and save max difference
        final reutrn max difference
        
        '''
        least = prices[0]
        output = 0
        for curr_price in prices[1:]:
            least = min(least, curr_price)
            output = max(output, curr_price - least)

        return output



























        # max_profit = 0
        # for price in prices[1:]:
        #     curr_min = min(curr_min, price)
        #     max_profit = max(max_profit, price-curr_min)
        # return max_profit