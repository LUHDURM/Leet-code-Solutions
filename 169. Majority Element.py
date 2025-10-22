class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for value in nums:
            hashmap[value] = 1 + hashmap.get(value,0)
        for num , count in hashmap.items():
            if count >= (len(nums)/2):
                return num
