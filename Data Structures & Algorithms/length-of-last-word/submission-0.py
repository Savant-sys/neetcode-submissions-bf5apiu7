class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                c += 1
            elif c > 0:
                break
                
        return c