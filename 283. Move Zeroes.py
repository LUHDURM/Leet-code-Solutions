class Solution(object):
    def moveZeroes(self, nums):
        Insert_pos = 0

        for num in nums:
            if num!=0:
                nums[Insert_pos]=num
                Insert_pos+=1

        while Insert_pos < len(nums):
            nums[Insert_pos]=0
            Insert_pos += 1        
        
