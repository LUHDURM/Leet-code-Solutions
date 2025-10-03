class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character = set()
        MAX = 0
        left = 0
        for right in range(len(s)):
            while s[right] in character:
                character.remove(s[left])
                left += 1
            character.add(s[right])
            MAX = max(MAX , len(character))
        return MAX  
