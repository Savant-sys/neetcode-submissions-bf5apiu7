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

        letters_s = {}
        letters_t = {}
        
        for i in range(len(s)):
            if s[i] not in letters_s:
                letters_s[s[i]] = 0
            letters_s[s[i]] += 1
            if t[i] not in letters_t:
                letters_t[t[i]] = 0
            letters_t[t[i]] += 1

        return letters_s == letters_t
        # for k in letters_s.keys():
        #     if k not in letters_t or letters_s[k] != letters_t[k]:
        #         return False

        # return True