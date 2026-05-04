class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] +=1
        
        for i in range(len(t)):
            if t[i] not in freq:
                return False
            freq[t[i]] -=1
        
        for letter in freq:
            if freq[letter] != 0 :
                return False
        return True
      