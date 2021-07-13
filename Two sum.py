class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                c = nums[i] + nums[j]
                if c == target:
                    l = []
                    l.append(i)
                    l.append(j)

                    return l
