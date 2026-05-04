class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            s = target - nums[i]

            if s in m:
                return [m[s], i]

            m[nums[i]] = i

        return []