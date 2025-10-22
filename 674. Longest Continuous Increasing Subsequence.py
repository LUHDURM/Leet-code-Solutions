class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length = 0
        count = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                length = max(count,length)
                count =1
        length = max(length,count)
        return length    
        
