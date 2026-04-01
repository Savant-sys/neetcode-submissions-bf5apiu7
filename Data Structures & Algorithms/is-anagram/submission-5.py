class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_strings= "".join(sorted(t))
        # sorted_stringt = "".join(sorted(s))

        # return True if sorted_strings == sorted_stringt else False
        




        

        # found = False
        # for c in s:
        #     for i in range(len(t)):
        #         if c == t[i]:
        #             found = True
        #             s = s[1:]
        #             t = t[:i] + t[i+1:]
        #             break
        #     if found == False:
        #         return found

        # if len(s) > 0 and len(t) > 0:
        #     return False
        # else:
        #     return True
        





        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countT == countS