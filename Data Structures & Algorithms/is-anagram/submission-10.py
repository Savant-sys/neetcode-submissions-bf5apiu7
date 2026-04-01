class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = 0
            if t[i] not in dct:
                dct[t[i]] = 0

            dct[s[i]] += 1
            dct[t[i]] -= 1

        for value in dct.values():
            if value > 0:
                return False

        return True
