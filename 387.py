class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 1:
            return 0
        
        check = dict()
        pas = list()
        for i in range(len(s)):
            letter = s[i]
            if letter in pas:
                continue
            if letter in check.keys():
                check.pop(letter)
                pas.append(letter)
            else:
                check[letter] = i
        if not check:
            return -1
        return sorted(list(check.values()))[0]