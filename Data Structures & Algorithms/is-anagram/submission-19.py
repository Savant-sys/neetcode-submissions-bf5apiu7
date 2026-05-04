class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = {}

        for c in s:
            m[c] = 1 + m.get(c, 0)

        for c in t:
            if c not in m:
                return False

            m[c] -= 1

            if m[c] < 0:
                return False

        return True