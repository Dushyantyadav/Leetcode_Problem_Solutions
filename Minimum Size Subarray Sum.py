class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        mylen=len(nums)+1
        mysum=0
        while i<len(nums):
            if mysum<target:
                mysum+=nums[i]
                i+=1
            while mysum>=target:
                if i-j<mylen:
                    mylen=i-j
                mysum-=nums[j]
                j+=1
        if mylen==len(nums)+1:
            return 0
        else:
            return mylen