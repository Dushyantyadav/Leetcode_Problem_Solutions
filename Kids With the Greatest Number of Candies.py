class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        myarr = []
        yarr = candies
        for i in range(0, len(candies)):
            x = extraCandies + candies[i]
            if x > max(yarr) or x == max(yarr):
                myarr.append(True)
            else:
                myarr.append(False)
        return myarr