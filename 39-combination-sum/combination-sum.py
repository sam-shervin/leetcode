class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, n):
                pick = candidates[i]
                backtrack(i, target-pick, path+[pick])
        backtrack(0, target,[])
        return result