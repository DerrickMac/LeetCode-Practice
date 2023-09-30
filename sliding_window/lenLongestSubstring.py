def lengthOfLongestSubstring(s):
        
        # declare an empty set to check for duplicates
        charSet = set()
        
        # initialize left pointer to 0
        l = 0

        # initialize result to 0
        res = 0

        # while current char is in the set
        for r in range(len(s)):
            while s[r] in charSet:
                # remove the left char and move left pointer
                charSet.remove(s[l])
                l += 1
            
            # add current char to set
            charSet.add(s[r])

            # update result
            res = max(res, r - l + 1)
        
        # return result
        return res