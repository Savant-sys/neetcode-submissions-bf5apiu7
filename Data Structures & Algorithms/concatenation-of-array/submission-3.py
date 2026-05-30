class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        hashset = []

        for i in range(2):
            for n in nums:
                hashset.append(n)

        return hashset