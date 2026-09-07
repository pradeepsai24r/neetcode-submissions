import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1. remove spaces and special chars
        nss = "".join([ns for ns in s if re.search(r'\w',ns)]).lower()

        print(nss)

        #2. check palindrome
        return nss == nss[::-1]
