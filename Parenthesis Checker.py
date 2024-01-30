class Solution:
    
    #Function to check if brackets are balanced or not.
   def ispar(self,x):
        # code here
        stack = []
        op = {'(','[','{'}
        cl = {')':'(',']':'[','}':'{'}
        
        for char in x:
            if char in op:
                stack.append(char)
            elif char in cl:
                if not stack or stack.pop() != cl[char]:
                    return False
        if not stack:
            return True