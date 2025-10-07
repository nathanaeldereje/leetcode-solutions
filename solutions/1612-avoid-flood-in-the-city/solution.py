from bisect import bisect_right

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        full_lakes = {}      # lake -> last day it was filled
        dry_days = []        # store indices of zero days
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)  # available to dry later
                ans[i] = 1          # placeholder
            else:
                if lake in full_lakes:
                    # find a dry day after last rain of this lake
                    j = bisect_right(dry_days, full_lakes[lake])
                    if j == len(dry_days):
                        return []  # no available dry day
                    dry_index = dry_days.pop(j)
                    ans[dry_index] = lake  # dry this lake
                full_lakes[lake] = i
        return ans

