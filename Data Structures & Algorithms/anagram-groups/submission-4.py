class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        for w in strs:
            freq = [0] * 26
            for c in w:
                i = ord(c) - ord("a")
                freq[i] += 1
            key = tuple(freq)
            if key not in res:
                res[key] = []
            res[key].append(w)

        return list(res.values())