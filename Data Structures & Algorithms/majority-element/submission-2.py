class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        element = 0

        for i in range(len(nums)):
            if c == 0:
                element = nums[i]
                c += 1

            elif element == nums[i]:
                c += 1
            else:
                c -= 1

        return element
        