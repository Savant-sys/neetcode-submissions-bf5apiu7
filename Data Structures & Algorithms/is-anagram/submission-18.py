class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dct = {}

        for c in s:
            dct[c] = 1 + dct.get(c, 0)

        for c in t:
            if c not in dct:
                return False
            dct[c] -= 1

            if dct[c] < 0:
                return False

        return True