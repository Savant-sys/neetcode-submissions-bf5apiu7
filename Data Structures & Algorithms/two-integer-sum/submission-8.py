class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # key = #
        # value = indices
        # key = target - n -> return key's value (index), current index
        for i, n in enumerate(nums):
            if target - n in hashmap:
                return [hashmap[target - n], i]

            hashmap[n] = i
