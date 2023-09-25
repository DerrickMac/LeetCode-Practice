def carFleet(target, position, speed):
    
    # for clarity, use list comprehension to 
    # make tuple pairs for each car's position and speed
    pair = [[p, s] for p, s in zip(position, speed)]
    
    # Reverse sort the list by position so we can simulate the one-lane restriction
    pair.sort(reverse=True)
    
    # Use stack data structure to compare the time it takes for each
    # car to reach the target. 
    stack = []
    for p, s in pair:
        stack.append((target - p) / s)
        
        # if car 1 has a faster time to get to the target, it means a fleet is formed
        # car 1 is going to move at the speed of car 2, that's why it gets popped from stack
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    
    # the len of stack represents the number of car fleets
    return len(stack)