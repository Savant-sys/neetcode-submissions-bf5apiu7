class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        word = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < len(word) and j < len(strs[i]) and word[j] == strs[i][j]:
                j += 1

            word = word[:j]

            if word == "":
                return ""

        return word