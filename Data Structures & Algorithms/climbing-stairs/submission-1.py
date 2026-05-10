class Solution:
    def climbStairs(self, n: int) -> int:
        i = 1
        j = 1

        for _ in range(n - 1):
            s = i + j
            i = j
            j = s

        return j



    # i + j = s

    # 1 + 1 = 2
    # 1 + 2 = 3
    # 2 + 3 = 5
    # 3 + 5 = 8