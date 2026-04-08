class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        r1 = len(matrix) - 1
        while l1 <= r1:
            l2 = 0
            r2 = len(matrix[l1]) - 1
            while l2 <= r2:
                m2 = (l2 + r2) // 2

                if matrix[l1][m2] > target:
                    r2 = m2 - 1
                elif matrix[l1][m2] < target:
                    l2 = m2 + 1
                else:
                    return True
            l1 += 1
        return False