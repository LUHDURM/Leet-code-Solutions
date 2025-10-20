class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for value in operations:
            if value == "++X" or value == "X++":
                count += 1
            else:
                count -= 1
        return count
        
