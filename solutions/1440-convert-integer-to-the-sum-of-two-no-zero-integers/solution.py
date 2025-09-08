class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        num1 = n - 1
        # Keep adjusting until both are no-zero
        while self.has_zero(num1) or self.has_zero(n - num1):
            num1 -= 1   # step down safely
        return [num1, n - num1]

    @staticmethod
    def has_zero(num: int) -> bool:
        while num > 0:
            if num % 10 == 0:
                return True
            num //= 10
        return False
