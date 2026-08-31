class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count=0
        n=len(arr)
        for i in range(n):
            a = 0
            for j in range(i + 1, n):
                a ^= arr[j - 1]
                b = 0
                for k in range(j, n):
                    b ^= arr[k]
                    if a==b:
                        count+=1
        return count

