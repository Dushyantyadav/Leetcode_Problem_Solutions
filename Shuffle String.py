class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        myarr=['']*len(s)
        for i in range(0,len(s)):
            myarr[indices[i]]=s[i]
        return ''.join(i for i in myarr)