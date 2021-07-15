class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_array=nums
        for i in range (0,len(nums)):
            new_array.append(nums[i])
        return new_array