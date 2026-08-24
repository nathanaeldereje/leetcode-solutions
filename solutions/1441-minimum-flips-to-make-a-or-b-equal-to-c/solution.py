class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        val=(a|b)
        zero_val=(~val & c).bit_count()
        zero_c=(val & ~c).bit_count()
        both_one = (a & b & ~c).bit_count()
        return (zero_val+zero_c+both_one)
        
