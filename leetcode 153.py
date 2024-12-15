from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        s=list(set(nums))
        s.sort()
        r=min(s)
        return r