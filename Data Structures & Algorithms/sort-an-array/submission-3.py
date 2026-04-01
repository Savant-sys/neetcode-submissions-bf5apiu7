class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # swapped = True
        # for i in range(len(nums)):
        #     swapped = False
        #     for j in range(len(nums) - i - 1):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #             swapped = True

        #     if swapped == False:
        #         break

        # return nums

        # return sorted(nums)
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res