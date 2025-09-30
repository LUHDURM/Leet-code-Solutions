class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while(len(nums)) > 1:
            num = []
            for i in range(len(nums)-1):
                Sum = nums[i] + nums[i+1]
                modulo = Sum % 10
                num.append(modulo)
            nums = num
        return nums[0]    
        
