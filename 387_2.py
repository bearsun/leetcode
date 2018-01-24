class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        single = dict()
        started = []
        for i in range(len(s)):
            letter = s[i]
            if letter not in started:
                started.append(letter)
                single[letter] = i
            else:
                single.pop(letter, None)
        if not single:
            return -1
        return min(single.values())