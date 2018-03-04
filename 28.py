class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if not needle:
            return 0
        
        for ih in range(len(haystack)-len(needle) + 1):
            if haystack[ih] == needle[0]:
                ind = 0
                bpass = False
                for ind in range(len(needle)):
                    if haystack[ih+ind] != needle[ind]:
                        bpass = True
                        break
                if not bpass:
                    return ih
        return -1