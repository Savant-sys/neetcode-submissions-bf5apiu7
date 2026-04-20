class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimum = nums[0]

        # for i in range(1, len(nums)):
        #     minimum = min(minimum, nums[i])

        # return minimum # this runs O(n)

        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                r -= 1
            elif nums[r] < nums[l]:
                l += 1

        if nums[l] < nums[r]:
            return nums[l]
        return nums[r]

            
