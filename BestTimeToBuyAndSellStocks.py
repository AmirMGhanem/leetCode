class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        _len=len(prices)

        max_profit=0
        min = prices[0]
        for i in range(1,_len):
            if prices[i]<min:
                min=prices[i]
            if prices[i]-min>max_profit:
                max_profit=prices[i]-min

        return max_profit





s= Solution()
prices=[3,10,1,5]
print(s.maxProfit(prices))