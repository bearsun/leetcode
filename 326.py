class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 2 and n == int(n):
            n = n/3
        if n == 1:
            return True
        return False