class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ord('a') - ord(c)


        res = {}

        for w in strs:
            count = [0] * 26

            for c in w:
                count[ord('a') - ord(c)] += 1

            if tuple(count) not in res:
                res[tuple(count)] = []

            res[tuple(count)].append(w)

        return list(res.values())