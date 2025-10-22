class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for value in nums:
            hashmap[value] = 1 + hashmap.get(value,0)
        for key , value in hashmap.items():
            if value == 1:
                return key
        
