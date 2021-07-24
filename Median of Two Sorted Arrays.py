class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p=0
        nums3=nums1+nums2
        nums3.sort()
        x=(len(nums3))%2
        if x==1:
            p=(len(nums3)//2)+1
            return float(nums3[p-1])
        if x==0:
            j=(len(nums3)//2)-1
            k=(len(nums3)//2)
            l=(nums3[j]+nums3[k])/2
            l=float(l)
            return l