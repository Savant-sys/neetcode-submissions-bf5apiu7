class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict:
        # key: [ord 26 alphabets counts]
        # value: ans
        res = {}

        for w in strs:
            freq = [0] * 26
            for c in w:
                freq[ord(c) - ord('a')] += 1
            k = tuple(freq)
            if k not in res:
                res[k] = []
            res[k].append(w)
        return list(res.values())
