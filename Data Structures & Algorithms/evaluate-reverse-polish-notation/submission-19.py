class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        set_ops = {"+", "*", "-", "/"}

        for i in range(len(tokens)):
            curr_token = tokens[i]
            if curr_token in set_ops:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if curr_token == "+":
                    stack.append(int(left_operand) + int(right_operand))
                elif curr_token == "-":
                    stack.append(int(left_operand) - int(right_operand))
                elif curr_token == "*":
                    stack.append(int(left_operand) * int(right_operand))
                else:
                    stack.append(int(int(left_operand) / int(right_operand)))
            else:
                stack.append(curr_token)
        
        print(stack)
        return int(stack[-1])