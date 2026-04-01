class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()

        res = strs[0]
        last = strs[-1]
        i = 0
        while i < len(res) and i < len(last) and res[i] == last[i]:
            i += 1

        return res[:i]
        # for i in range(1, len(strs)):
            

            # j = 0
            # while j < len(res) and j < len(strs[i]) and res[j] == strs[i][j]:
            #     j += 1
            
            # res = res[:j]
               

        # return res