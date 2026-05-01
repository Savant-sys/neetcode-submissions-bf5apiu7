class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        r1 = len(matrix) - 1
        while l1 <= r1:
            l2 = 0
            r2 = len(matrix[l1]) - 1

            while l2 <= r2:
                mid = (l2 + r2) // 2

                if matrix[l1][mid] < target:
                    l2 = mid + 1
                elif matrix[l1][mid] > target:
                    r2 = mid - 1
                else:
                    return True
            l1 += 1
        return False