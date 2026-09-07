from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w1 in strs:
            k = "".join(sorted(w1))
            if k in d:
                d[k].append(w1)
            else:
                d[k]=[w1]
        return list(d.values())


