class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        myarr = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if nums[i] > nums[j] and j != i:
                    count = count + 1
            myarr.append(count)
        return myarr