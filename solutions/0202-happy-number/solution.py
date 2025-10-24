class Solution:
    def isHappy(self, n: int) -> bool:
        memo = {}  # store sum-of-squares results

        def next_num(x: int):
            if x in memo:
                return memo[x]
            total = 0
            y = x
            while y:
                total += (y % 10) ** 2
                y //= 10
            memo[x] = total
            return total

        slow, fast = n, next_num(n)
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1

