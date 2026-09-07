from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cm = Counter(nums) # {'1':2, '2': 1, '3': 3}
        return [n for n,_ in cm.most_common(k)]