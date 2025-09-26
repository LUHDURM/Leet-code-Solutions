class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        k = len(nums)
        for i in range(k-1,1,-1):
            l , r = 0 , i-1
            while l < r:
                if nums[l]+nums[r] > nums[i]:
                    count += (r-l)
                    r -= 1
                else:
                    l += 1
        return count         

        
