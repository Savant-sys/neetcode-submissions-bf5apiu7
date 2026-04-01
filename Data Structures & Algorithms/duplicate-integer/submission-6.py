class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            digit = nums[i]

            for j in range(i + 1, len(nums)):
                if digit == nums[j]:
                    return True

        return False