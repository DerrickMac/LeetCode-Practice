def isValid(s):
    end_brackets = {")": "(", "}": "{", "]": "["}

    stack = []

    for bracket in s:

        # if we found a closing bracket:        
        if bracket in end_brackets:

            # if stack is not empty
            # and found a matching closing bracket with top of stack
            if stack and stack[-1] == end_brackets[bracket]:
                stack.pop()
            
            # if stack is empty or did not find a matching closing bracket, invalid answer
            else:
                return False

        # if found an open bracket, then add to stack
        else:
            stack.append(bracket)


