class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        best = 0
        current = 1
        previous = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                current += 1
            else:
                best = max(best , current//2 , min(current,previous))
                previous = current
                current = 1
        best = max(best , current//2 , min(current,previous))
        return best
        
