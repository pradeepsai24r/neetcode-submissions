from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hc = Counter(nums)
        return [n for n,_ in hc.most_common(k)]