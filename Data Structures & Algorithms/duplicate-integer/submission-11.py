class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = set()

        for n in nums:
            if n in lst:
                return True
            lst.add(n)

        return False