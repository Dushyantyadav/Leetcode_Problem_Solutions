class Solution:
    def judgeCircle(self, moves: str) -> bool:
        strt = [0, 0]

        for i in moves:
            if i == 'U':
                strt[1] += 1
            elif i == 'D':
                strt[1] -= 1
            elif i == 'R':
                strt[0] += 1
            elif i == 'L':
                strt[0] -= 1

        return strt == [0, 0]