class Solution:
    def longestPalindrome(self, s: str) -> str:
        mystr = ""
        mystrlen = 0
        for i in range(0, len(s)):
            lft, rt = i, i
            while lft >= 0 and rt < len(s) and s[lft] == s[rt]:
                if (rt - lft + 1) > mystrlen:
                    mystr = s[lft:rt + 1]
                    mystrlen = rt - lft + 1
                lft -= 1
                rt += 1
            lft, rt = i, i + 1
            while lft >= 0 and rt < len(s) and s[lft] == s[rt]:
                if (rt - lft + 1) > mystrlen:
                    mystr = s[lft:rt + 1]
                    mystrlen = rt - lft + 1
                lft -= 1
                rt += 1

        return mystr