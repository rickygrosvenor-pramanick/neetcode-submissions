class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # stack of indicies
        stack = [0]
        i = 1

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]
            num_to_adjust = 0
            if curr_temp <= temperatures[stack[-1]]:
                stack.append(i)
                continue

            while len(stack) > 0 and curr_temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
                num_to_adjust += 1
            
            stack.append(i)
        
        return result

            



        
