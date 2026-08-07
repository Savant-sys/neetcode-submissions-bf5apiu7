class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = nums[mid:]
        right = nums[:mid]

        sortedLeft = self.sortArray(left)
        sortedRight = self.sortArray(right)

        print("left", sortedLeft)
        print("right", sortedRight)

        return self.merge(sortedLeft, sortedRight)

    def merge(self, left, right):
        i = j = 0
        res = []

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