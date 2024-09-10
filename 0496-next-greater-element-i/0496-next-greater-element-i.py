class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = list()
        flag = True
        for i in nums1:
            for j in nums2[nums2.index(i)+1:]:
                if j>i:
                    flag = False
                    a.append(j)
                    break
            if flag:
                a.append(-1)
            flag = True
        return a
                    
        
        