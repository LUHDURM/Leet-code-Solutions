class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = needle[0:]
        return haystack.find(a)
        
