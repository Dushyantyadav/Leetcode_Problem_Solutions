class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = []
        d = []
        for i in jewels:
            c.append(i)
        for j in stones:
            d.append(j)
        count = 0
        for l in range(0, len(c)):
            for m in range(0, len(d)):
                if c[l] == d[m]:
                    count += 1
        return count