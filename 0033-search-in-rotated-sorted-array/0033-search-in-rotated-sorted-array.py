class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #4, 5, 6, 7, 0, 1, 2    search 1 -- start>1, middle>1, middle<start -- left
                                #search 1 -- start >1, middle>1, middle>start -- right
                                #search 1 -- start>1, middle<1, middle<start, -- left
                                #search 1 -- start>1, middle<1, middle>start -- right
                                #search 5 -- start<5, middle>5 -- left
                                            #start<5, middle<5 -- right

        a = 0
        b = len(nums)-1
        while(a<=b):
            mid = (a+b)//2
            nm = nums[mid]
            na = nums[a]
            if target == nm:
                return mid
            elif (nums[a] <= nm and nums[a] <= target < nm) or (nums[a] > nm and (target < nm or target >= nums[a])):
                b = mid-1
            else:
                a = mid+1
        return -1
            