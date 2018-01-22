class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = list(s)
        base = ord('A')-1
        
        total = 0
        digit = 0
        for letter in ls[::-1]:
            total += (ord(letter)-base) * (26**digit)
            digit += 1
            
        return total