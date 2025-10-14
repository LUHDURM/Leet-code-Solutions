class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        best = 0
        previous = 0
        current = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                current += 1
            else:
                best = max(best , current//2 , min(previous,current))
                previous = current
                current = 1
        best = max(best , current//2 , min(current,previous))
        return best >= k
        
