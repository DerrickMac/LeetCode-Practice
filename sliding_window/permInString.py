def checkInclusion(s1, s2):

    # longer str s1 will mean invalid solution
    if len(s1) > len(s2):
        return False

    # create two arrays at length 26 to store counts    
    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        # use ord function to calculate each letter's index within the count array size of 26
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    # initialize number of matches and iterate through both arrays to update matches 
    matches = 0
    for i in range(26):
        if s1Count[i] == s2Count[i]:
            matches += 1
    
    # Use a sliding window to incrementally check if all chars in s1 are included in s2
    # by expanding window right bound and contracting left bound each iteration.
    l = 0
    for r in range(len(s1), len(s2)): # each for loop iteration is a right bound expansion
        if matches == 26:
            return True
        
        # update counts and matches when right window expands
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1
        
        # update counts and matches when left window contracts
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1

        # manually contract left bound window
        l += 1

    # return expression True when there are 26 matches
    return matches == 26
    
    
            