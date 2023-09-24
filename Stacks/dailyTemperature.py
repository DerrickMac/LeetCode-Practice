def dailyTemp(arr):
    
    # create an array of 0's
    result = [0] * len(arr)
    
    # initialize a stack
    stack = [] # pair: [temp, index]

    # Iterate through the array once, saving the temp and its index, so we can check whether the next temperature is greater
    # Every time we find a larger temp, we pop the stack and update the result array with the difference between the current index and the popped index.
    for i, t in enumerate(arr):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            result[stackInd] = (i - stackInd)
        stack.append([t, i])
    
    # we will return the resulting array at the end
    # in the case a day doesn't have a warmer day, the result array already has 0's initialized in its place so nothing needs to be updated in these cases.
    return result



    




    
    
