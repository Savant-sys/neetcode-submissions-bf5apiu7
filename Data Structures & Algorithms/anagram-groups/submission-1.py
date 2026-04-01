class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for w in strs:
            count = [0] * 26 
            for c in w:
                # print(ord(c))
                # print(ord('a'))
                # print(ord(c) - ord('a'))
                count[ord(c) - ord('a')] += 1

            if tuple(count) not in res:
                res[tuple(count)] = []

            print("tuple: ", tuple(count))
            res[tuple(count)].append(w)
        
        return list(res.values())