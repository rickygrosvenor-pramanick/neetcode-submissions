class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # stack of indicies
        stack = [0]

        for i in range(1, len(temperatures)):
            curr_temp = temperatures[i]
            if curr_temp <= temperatures[stack[-1]]:
                stack.append(i)
                continue

            while len(stack) > 0 and curr_temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            
            stack.append(i)
        
        return result

            



        
