class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack:
                top = stack[-1]
                if temperatures[top] >= temp:
                    break
                stack.pop()
                res[top] = i - top
            stack.append(i)
        return res
