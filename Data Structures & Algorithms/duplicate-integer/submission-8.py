class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicated = []

        for n in nums:
            if n in duplicated:
                return True
            duplicated.append(n)

        return False