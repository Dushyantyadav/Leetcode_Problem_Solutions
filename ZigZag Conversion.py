class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = 0
        mylst = [[] for i in range(len(s))]

        var1 = -1
        for j in s:
            mylst[r].append(j)
            if r == 0 or r == numRows - 1:
                var1 *= -1
            r += var1
        for i in range(len(mylst)):
            mylst[i] = ''.join(mylst[i])
        return ''.join(mylst)