class Solution:
    """
    PS: "<str>" ---> CODE --> <int> (count of non-reteating chars)
    inputs:
    "" (empty) --> 0
    "a" -->  1
    "ab" --> 2
    "aaa" --> 1
    "abcd" --> 4
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        cc = 0
        for i, x in enumerate(s):
            while x in seen:
                seen.remove(s[l])
                l += 1
            seen.add(x)
            cc = max(cc, i-l+1)
        return cc

    def lengthOfLongestSubstring1(self, s: str) -> int:
        tc = 0
        mc = 0
        seen = set()
        for x in s:
            if x not in seen:
                tc += 1
                seen.add(x)
            else:
                mc = max(mc,tc)
                tc = 1
        return max(tc,mc)
