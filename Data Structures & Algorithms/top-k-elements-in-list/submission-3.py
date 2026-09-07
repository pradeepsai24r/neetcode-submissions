from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        count_map = Counter(nums)
        return [num for num, _ in count_map.most_common(k)]

