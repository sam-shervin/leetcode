class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)//2
        return (nums1[length-1]+nums1[length])/2 if len(nums1)%2==0 else nums1[length]


