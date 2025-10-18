class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i,num in enumerate(nums):
            compliment = target-num
            if compliment in hashmap:
                return [hashmap[compliment],i]
            hashmap[num]=i  
        
