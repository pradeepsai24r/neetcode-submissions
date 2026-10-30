from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        td = {}
        for x in nums:
            if x in td:
                td[x] += 1
            else:
                td[x] = 1
        sh = sorted(td.items(), key=lambda i:i[1], reverse= True)
        res = [n for n,_ in sh[:k]]
        return res

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        cm = Counter(nums) # {'1':2, '2': 1, '3': 1} number: count
        return [n for n,_ in cm.most_common(k)] ## [(1, 2), (2, 1), (3, 1)]