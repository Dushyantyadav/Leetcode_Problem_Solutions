class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        p=len(rating)
        for i in range(0,p-2):
            for j in range(i+1,p-1):
                for k in range(j+1,p):
                    if rating[i]>rating[j]>rating[k] or rating[i]<rating[j]<rating[k]:
                        count=count+1
        return count