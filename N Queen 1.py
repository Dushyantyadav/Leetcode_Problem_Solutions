class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mycol=set()
        posdiag=set()
        negdiag=set()
        res=[]
        mybrd=[["."]*n for i in range(n)]
        
        def mybacktrack(r):
            if r==n:
                mycopy=["".join(row) for row in mybrd]
                res.append(mycopy)
                return mybrd
            for c in range(n):
                if c in mycol or r-c in negdiag or r+c in posdiag:
                    continue
                mycol.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                mybrd[r][c]="Q"

                mybacktrack(r+1)
                
                mycol.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                mybrd[r][c]="."
        mybacktrack(0)
        return res