class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        element = 0

        for n in nums:
            if c == 0:
                element = n
                c += 1

            elif element == n:
                c += 1
            else:
                c -= 1

        return element
        