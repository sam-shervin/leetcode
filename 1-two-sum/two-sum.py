class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] in hashmap.keys():
                return [hashmap[nums[i]], i]
            else:
                hashmap[target-nums[i]] = i
