class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {} # value: index

        for i in range(len(nums)):
            if nums[i] in dct:
                return [dct[nums[i]], i]
            ans = target - nums[i]
            dct[ans] = i

        return -1