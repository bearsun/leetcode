class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I': 1}
        total = 0
        cur = 'M'
        digitlist = ['I','V','X','L','C','D']
        ls = list(s)
        while ls:
            if cur in ls:
                icur = ls.index(cur)
                if icur > 0: #smaller digit on the left
                    for i in range(icur):
                        total -= digit[ls[i]]
                total += digit[ls[icur]]
                ls = ls[(icur+1):]
            else:
                cur = digitlist.pop()      
        return total