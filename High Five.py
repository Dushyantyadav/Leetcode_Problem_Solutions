class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        g=[]
        for i in items:
            g.append(i[0])
        g=set(g)
        g=list(g)
        h=[[] for x in g]
        k=0
        for j in g:
            q=0
            p=[]
            for i in items:
                if i[0]==j:
                    p.append(i[1])
            p.sort(reverse=True)
            for i in range(0,5):
                q=q+p[i]
            q=int(q/5)
            h[k].append(j)
            h[k].append(q)
            k=k+1
        return h