class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_array = []
        for i in range(0, len(nums)):
            new_array.append(nums[nums[i]])
        return new_array
