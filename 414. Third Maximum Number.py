class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        Nums = sorted(set(nums))
        if len(Nums) < 3:
            return Nums[-1]
        return Nums[-3]
    
