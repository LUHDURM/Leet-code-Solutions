class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums.count(val) == 0:
            return len(nums)
        while nums.count(val) != 0:
            nums.remove(val)
