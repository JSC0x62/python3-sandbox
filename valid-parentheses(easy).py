# https://leetcode.com/problems/valid-parentheses
# https://www.youtube.com/watch?v=WTzjTskDFMg
# O(n) solution
class Solution:
    def isValid(self, s: str) -> bool:
        #HashMap that maps each closing paren to its opening match. Makes validating much easier.
        closeToOpenMap = {")" : "(", "]" : "[", "}" : "{"}
        # Stack is used to keep track of the parentheses. Need to work from "inside out" so stack is better than queue here.
        stack = []
        
        # For the current element in the str
        for currStr in s:
            # If we hit a closing paren
            if currStr in closeToOpenMap:
                # If the stack is not null, and the top of the stack ([-1] does this) is = to the corresponding opening paren of the value being checked, there is a match
                if stack and stack[-1] == closeToOpenMap[currStr]:
                    # Pop that value off and continue checking
                    stack.pop()
                # This means there was a closing paren but it was mapped to the wrong value
                else:
                    return False
            # In this case there was an opening paren and its added to the stack
            else:
                stack.append(currStr)
        # The stack must be empty at the end
        return True if not stack else False
