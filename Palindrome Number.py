class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        c=[]
        for i in y:
            c.append(i)
        c.reverse()
        p=''.join(c)
        if y==p:
            return True
        else:
            return False