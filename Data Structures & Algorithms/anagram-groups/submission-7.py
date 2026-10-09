class Solution:
    ## BrutFroce
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     for w in strs:
    #         for c in w:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for w in strs:
            k = "".join(sorted(w))
            if k in d:
                d[k].append(w)
            else:
                d[k]=[w]
        return list(d.values())