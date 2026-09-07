from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ot = {}
        for w in strs:
            sw = "".join(sorted(w))
            if sw in ot:
                ot[sw].append(w)
            else:
                ot[sw]=[w]
        return list(ot.values())


