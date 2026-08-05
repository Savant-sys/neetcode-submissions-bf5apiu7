class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        element = None

        for n in nums:
            if c == 0:
                element = n
            
            if element == n:
                c += 1
            else:
                c -= 1

        return element