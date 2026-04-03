class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        res = ""

        for w in strs:
            res += str(len(w)) + ","

        res += "#"

        for w in strs:
            res += w

        return res

        return enc
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        sizes = []
        i = 0

        while s[i] != "#":
            num = ""
            while s[i] != ",":
                num += s[i]
                i += 1
            sizes.append(int(num))
            i += 1
        i += 1

        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res