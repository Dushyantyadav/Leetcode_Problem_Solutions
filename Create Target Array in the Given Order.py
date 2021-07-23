class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        tar = []
        for i in range(0, len(nums)):
            tar.insert(index[i], nums[i])
        return tar