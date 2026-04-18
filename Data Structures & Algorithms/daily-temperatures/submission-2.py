class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            today_temp = temperatures[i]
            if not stack:
                stack.append([today_temp, i])
            else:
                if stack[-1][0] < today_temp:
                    print(stack)
                    while len(stack) > 0:
                        if stack[-1][0] < today_temp:
                            popped = stack.pop()
                            result[popped[1]] = i - popped[1]
                        else:
                            break
                    stack.append([today_temp, i])
                else:
                    stack.append([today_temp, i])
        
        return result