class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        main=0
        for i,h in enumerate(heights):
            start = i
            while(stack and stack[-1][1] > h):
                index, height=stack.pop()
                main=max(main, height * (i - index))
                start=index
            stack.append((start, h))
        for i, h in stack:
            main = max(main, h * (len(heights) - i))
        return main
