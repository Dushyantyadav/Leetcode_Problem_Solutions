class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        myarr = []
        p = len(nums)
        k = 0
        while (2 * k + 1) < len(nums):
            myvar = nums[2 * k]
            myvar2 = nums[2 * k + 1]
            for l in range(0, myvar):
                myarr.append(myvar2)
            k += 1
        return myarr