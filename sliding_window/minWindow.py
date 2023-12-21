def minWindow(s, t):
    if len(t) > len(s):
        return ""
    
    countT, window = {}, {}

    # initialize countT map
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    
    l = 0
    for r in range(len(s)):
        
        # get current char
        c = s[r]
        
        # Update window map 
        window[c] = 1 + window.get(c, 0)

        # Check if current char in countT and does window have same count as countT
        if c in countT and window[c] == countT[c]:
            have += 1
        
        # after met condition above, update
        while have == need:
            
            # if current length of string is less than current resLen, set result to current window
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            
            # pop from the left of our window to keep window as small as it can be
            window[s[l]]-= 1

            # decrement have count if we removed a char from window that is in countT
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
        
    l, r = res
    return s[l:r+1] if resLen != float("infinity") else ""
