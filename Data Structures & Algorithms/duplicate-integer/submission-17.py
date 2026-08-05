class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []

        for n in nums:
            if n in temp:
                return True
            temp.append(n)

        return False