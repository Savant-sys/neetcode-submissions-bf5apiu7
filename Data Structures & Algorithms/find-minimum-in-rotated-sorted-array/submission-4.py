class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimum = nums[0]

        # for i in range(1, len(nums)):
        #     minimum = min(minimum, nums[i])

        # return minimum # this runs O(n)

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

            
