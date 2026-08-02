class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h = {}

        for c in s:
            h[c] = 1 + h.get(c, 0)

        for c in t:
            if c not in h:
                return False
            h[c] -= 1
            if h[c] < 0:
                return False

        return True