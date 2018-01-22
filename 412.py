class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = list()
        for i in range(1,n+1):
            cur = []
            if i % 3 == 0:
                cur.append('Fizz')
            if i % 5 == 0:
                cur.append('Buzz')
            if not cur:
                cur.append(str(i))
            out.append(''.join(cur))
        return out