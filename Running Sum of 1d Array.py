class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_array=[]
        mysum=0
        for i in range(0,len(nums)):
            mysum=mysum+nums[i]
            new_array.append(mysum)
        return new_array