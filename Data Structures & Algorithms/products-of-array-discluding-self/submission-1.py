class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # [48, 24, 12, 8]

        prefix = 1 # 48

        for i in range(len(nums)): # 3
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # 0
            res[i] *= postfix
            postfix *= nums[i]

        # print(res)

        return res          
            