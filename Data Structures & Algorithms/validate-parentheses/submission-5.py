class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        num_square_open, num_square_closed = 0, 0
        num_curve_open, num_curve_closed = 0, 0
        num_squiggle_open, num_squiggle_closed = 0,0
        
        for c in s:
            if c in {"[", "{", "("}:
                stack.append(c)
                if c == "[":
                    num_square_open += 1
                elif c == "(":
                    num_curve_open += 1
                else:
                    num_squiggle_open += 1
            else:
                if not stack:
                    return False
                if c == "}" and stack[-1] != "{":
                    return False
                if c == ")" and stack[-1] != "(":
                    return False
                if c == "]" and stack[-1] != "[":
                    return False
                if c == "}":
                    num_squiggle_closed += 1
                    stack.pop()
                elif c == ")":
                    num_curve_closed += 1
                    stack.pop()
                elif c == "]":
                    num_square_closed += 1
                    stack.pop()
                
        
        if num_square_open == num_square_closed and num_curve_open == num_curve_closed and num_squiggle_open == num_squiggle_closed and len(stack) == 0:
            return True
        else:
            return False