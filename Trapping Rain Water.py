class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        ltmax, rtmax = height[l], height[r]
        myr = 0
        while l < r:
            if ltmax < rtmax:
                l += 1
                ltmax = max(ltmax, height[l])
                myr += ltmax - height[l]
            else:
                r -= 1
                rtmax = max(rtmax, height[r])
                myr += rtmax - height[r]
        return myr
