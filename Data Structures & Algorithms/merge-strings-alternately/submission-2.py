class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0

        while i < len(word1) and i < len(word2):
            if i < len(word1):
                # res += word1[i]
                res.append(word1[i])
            if i < len(word2):
                # res += word2[i]
                res.append(word2[i])
            i += 1

        res.append(word1[i:])
        res.append(word2[i:])

        return "".join(res)