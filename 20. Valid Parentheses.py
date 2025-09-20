class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {')':'(','}':'{',']':'['}

        for char in s:
            if char in mapping:
                Top = stack.pop() if stack else '#'
                if mapping[char] != Top:
                    return False
            else:
                stack.append(char)
        return not stack                
        
