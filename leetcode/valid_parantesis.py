class Solution(object):
    def isValid(self, s):
        stack = []

        brackets = {")": "(", "}": "{", "]": "["}

        for b in s:
            if not stack and b in brackets:
                return False
            elif b in brackets:
                if stack.pop() != brackets[b]:
                    return False
            else:
                stack.append(b)
        return True if not stack else False



class Solution(object):
    def isValid(self, s):
        stack=[]
        for char in s:
            if char in '[{(':
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if ((char == ')' and top!='(') or (char == '}' and top!='{') or (char == ']' and top!='[')):
                    return False
        return not stack             
    
"""
Input: s = "()[]{}"
Output: true    
"""