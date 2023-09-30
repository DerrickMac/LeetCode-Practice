def maxProfit(prices):
    # initialize two pointers l = 0 (buy), r = 1 (sell)
    l, r = 0, 1

    # set max profit to 0 
    maxP = 0

    while r < len(prices):            
        # When there is profit, update the max profit if necessary
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            # in the case that the transaction is not profitable, update the l pointer to the right pointer
            # l pointer represents the cheapest price to buy stock
            l = r
        
        # sliding window: move r pointer to compute transactions of each day      
        r += 1
    
    return maxP