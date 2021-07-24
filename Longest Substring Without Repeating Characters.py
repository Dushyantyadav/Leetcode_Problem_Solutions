class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=0
        end=0
        maxlen=0
        d={}
        while end<len(s):
            if s[end] in d and d[s[end]]>=st:
                st=d[s[end]]+1
            maxlen=max(maxlen,end-st+1)
            d[s[end]]=end
            end+=1
        return maxlen