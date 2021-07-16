class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        myarr = []
        for i in range(0, n):
            myarr.append(nums[i])
            myarr.append(nums[i + n])
        return myarr