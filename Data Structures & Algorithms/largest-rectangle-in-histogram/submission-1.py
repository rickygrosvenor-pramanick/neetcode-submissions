class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)):
            if not stack:
                stack.append((i, heights[i]))
                continue
            
            curr_height = heights[i]
            if curr_height > stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                prev = None
                while curr_height <= stack[-1][1]:
                    prev = stack.pop()
                    max_area = max(max_area, (i - prev[0]) * prev[1])
                    if len(stack) == 0:
                        break
                stack.append((prev[0], heights[i]))
        
        for idx, height in stack:
            max_area = max(max_area, (len(heights) - idx) * height)
        return max_area

