class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        grabber = []

        for i in range(len(nums)):
            if nums[i] in grabber:
                return True
            grabber.append(nums[i])

        return False