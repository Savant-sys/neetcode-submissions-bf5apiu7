class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if target == matrix[i][j]:
                    return True
                j += 1
            i += 1

        return False