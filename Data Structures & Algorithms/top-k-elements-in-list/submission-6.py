from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tc = Counter(nums)
        return [n for n,_ in tc.most_common(k)]