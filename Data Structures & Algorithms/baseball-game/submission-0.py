class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for ops in operations:
            if ops == "+":
                res.append(res[-1] + res[-2])
                continue
            if ops == "C":
                res.pop()
                continue
            if ops == "D":
                res.append(res[-1] * 2)
                continue
            res.append(int(ops))

        return sum(res)
            