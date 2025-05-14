class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        nums.sort()
        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap[i] = True
        return False
            
        