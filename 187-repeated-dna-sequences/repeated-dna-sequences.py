class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        mapping = {'A':0, 'C':1, 'G':2, 'T':3}
        seen, repeated = set(), set()
        hash_val = 0
        
        for i, ch in enumerate(s):
            # shift left 2 bits and add new char
            hash_val = ((hash_val << 2) | mapping[ch]) & ((1 << 20) - 1)
            
            if i >= 9:  # window of size 10
                if hash_val in seen:
                    repeated.add(s[i-9:i+1])
                else:
                    seen.add(hash_val)
                    
        return list(repeated)
