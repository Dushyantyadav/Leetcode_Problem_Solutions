class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        mydir = (0, 1)
        strt = [0, 0]

        for i in range(0, 4):
            for x in instructions:
                if x == 'G':
                    strt[0] += mydir[0]
                    strt[1] += mydir[1]
                elif x == 'L':
                    mydir = (-mydir[1], mydir[0])
                elif x == 'R':
                    mydir = (mydir[1], -mydir[0])
        return strt == [0, 0]