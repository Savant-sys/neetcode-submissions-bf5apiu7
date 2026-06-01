class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        for c in s:
            hashmap[c] = 1 + hashmap.get(c, 0)

        for c in t:
            if c not in hashmap:
                return False

            hashmap[c] -= 1

            if hashmap[c] < 0:
                return False
            
        return True