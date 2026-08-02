class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        # s = target - nums[i]
        # hashmap[s] = i

        for i, n in enumerate(nums):
            s = target - n
            if s in m:
                return [m[s], i]
            
            m[n] = i