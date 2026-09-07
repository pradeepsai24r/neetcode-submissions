class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for w in strs:
            sw = "".join(sorted(w))
            if sw in s:
                s[sw].append(w)
            else:
                s[sw] = [w]
        return list(s.values())
