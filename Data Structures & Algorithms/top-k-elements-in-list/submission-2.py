class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for n in nums:
            m[n] = 1 + m.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in m.items():
            freq[count].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if k == len(res):
                    return res