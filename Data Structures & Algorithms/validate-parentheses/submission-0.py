class Solution:
    def isValid(self, s: str) -> bool:
        rules = {')': '(', '}': '{', ']': '['}

        arr = []
        for c in s:
            if c not in rules:
                arr.append(c)
            else:
                if len(arr) > 0 and arr[-1] == rules[c]:
                    arr.pop(-1)
                else:
                    return False

        return len(arr) == 0