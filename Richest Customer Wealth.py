class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        myarr = []
        for i in range(0, len(accounts)):
            mysum = 0
            for j in range(0, len(accounts[0])):
                mysum = mysum + accounts[i][j]
            myarr.append(mysum)
        c = max(myarr)
        return c

