class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(0, len(heights)):
            if not stack:
                stack.append((i, heights[i]))
                continue
            
            if heights[i] > stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                prev = None
                while heights[i] <= stack[-1][1]:
                    prev = stack.pop()
                    max_area = max(max_area, (i - prev[0]) * prev[1])
                    if len(stack) == 0:
                        break
                stack.append((prev[0], heights[i]))
        
        for pair in stack:
            max_area = max(max_area, (len(heights) - pair[0]) * pair[1])
        
        return max_area
            



