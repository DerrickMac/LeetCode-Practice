def characterReplacement(s, k):
    count = {}
    res = 0
    l = 0

    for r in range(len(s)):
        # Increment count for each letter, or create new entry in count dictionary and set to 0
        count[s[r]] = 1 + count.get(s[r], 0)

        
        # if we encounter an invalid window, then shift left pointer until window is valid, update count dictionary
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        
        # if the window size - the max value of count dictionary <= k (valid window)
        # update result
        res = max(res, r - l + 1)
    return res


# more optimal solution O(n)

def characterReplacement(s, k):
    count = {}
    res = 0
    l = 0
    maxf = 0

    for r in range(len(s)):
        # Increment count for each letter, or create new entry in count dictionary and set to 0
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        
        # if we encounter an invalid window, then shift left pointer until window is valid, update count dictionary
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        
        # if the window size - the max value of count dictionary <= k (valid window)
        # update result
        res = max(res, r - l + 1)
    return res