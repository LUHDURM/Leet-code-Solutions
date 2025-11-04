class Solution:
    def intToRoman(self, num: int) -> str:
        i = 0
        roman = ""
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        values = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        while num > 0:
            count = num // nums[i]
            roman += values[i] * count
            num -= nums[i] * count
            i += 1
        return roman
        
