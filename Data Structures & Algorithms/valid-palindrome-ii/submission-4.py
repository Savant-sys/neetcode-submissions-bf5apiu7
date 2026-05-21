class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(l, r):
            while l < r:
                if not s[l].isalnum():
                    l += 1

                if not s[r].isalnum():
                    r -= 1

                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
                
            return True
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l].lower() != s[r].lower():
                return isValid(l + 1, r) or isValid(l, r - 1)

            l += 1
            r -= 1


        return True
                