class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_strings= "".join(sorted(t))
        sorted_stringt = "".join(sorted(s))

        return True if sorted_strings == sorted_stringt else False
        
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
        
        # letters_s = {}
        # letters_t = {}
        # for c in s:
        #     if c not in letters_s:
        #         letters_s[c] = 0
        #     letters_s[c] += 1

        # for c in t:
        #     if c not in letters_t:
        #         letters_t[c] = 0
        #     letters_t[c] += 1

        # if len(letters_s) < len(letters_s) or len(letters_s) > len(letters_s):
        #     return False

        
        # for k in letters_s.keys():
        #     if k not in letters_t or letters_s[k] != letters_t[k]:
        #         return False

        # return True