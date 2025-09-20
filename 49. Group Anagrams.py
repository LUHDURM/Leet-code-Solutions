class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            SS = ''.join(sorted(s))
            res[SS].append(s)
        return list(res.values())    
        
