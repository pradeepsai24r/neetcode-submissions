from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_h = Counter(nums)
        for k,v in nums_h.items():
            if v == 1:
                return k
        