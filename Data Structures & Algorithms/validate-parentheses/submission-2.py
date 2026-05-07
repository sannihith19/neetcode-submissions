class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}": "{", "]": "["}
        stack = []
        for bracket in s:
            if bracket in pairs:
                if stack and pairs[bracket] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
                
            stack.append(bracket)
        return not stack 
