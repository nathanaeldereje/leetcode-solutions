from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        prev = set()

        for num in arr:
            curr = set()
            curr.add(num)  # single element subarray

            for val in prev:
                curr.add(val | num)  # extend previous subarrays

            res.update(curr)
            prev = curr  # update for next iteration

        return len(res)

