class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        store = set(nums)
        for num in store:
            if (num - 1) not in store:
                l = 1
                while (num + l) in store:
                    l += 1
                res = max(res,l)
        return res            
              
        
