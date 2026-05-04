class Solution:
    def alphaNum(self, c):
        return c.isalnum()

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l,r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l+=1
            while l <r and not self.alphaNum(s[r]):
                r-=1
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True