class Solution:
    def isValid(self, s: str) -> bool:
        num_open, num_closed = 0, 0
        num_curly_open, num_curly_closed = 0, 0
        num_square_open, num_square_closed = 0, 0

        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                num_open += 1
                stack.append(s[i])
            elif s[i] == ")":
                num_closed += 1
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif s[i] == "{":
                num_curly_open += 1
                stack.append(s[i])
            elif s[i] == "}":
                num_curly_closed += 1
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            elif s[i] == "[":
                num_square_open += 1
                stack.append(s[i])
            elif s[i] == "]":
                num_square_closed += 1
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
        
        if len(stack) != 0:
            return False
        # if num_closed != num_open or num_curly_closed != num_curly_open or num_square_closed != num_square_open:
        #     return False
        
        return True
            
            