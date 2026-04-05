class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and heights[stack[-1][0]] > h:
                idx, width_start = stack.pop()
                area = heights[idx] * (i - width_start)
                max_area = max(area, max_area)
                start = width_start
            stack.append((i,start))

        for i, start in stack:
            area = heights[i] * (len(heights) - start)
            max_area = max(max_area, area)

        return max_area