import math

def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    result = r
    
    def eatingTime(piles, k):
        curr_h = 0
        for pile in piles:
            curr_h += math.ceil(pile / k)
        return curr_h

    while l <= r:
        k = (l + r) // 2
        eat_time = eatingTime(piles, k)
        
        # if k's eating time < h,  then r needs to shift to left to attain a higher h.
        if eat_time <= h:
            result = min(result, k)
            r = k - 1

        else:
            # if k's eating time > h, then l needs to shift to right to attain a lower h.
            l = k + 1
    
    return result

# test input
piles = [312884470]
h = 312884469

print(minEatingSpeed(piles, h))