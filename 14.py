class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        pre = ''
        icol = 0
        nrow = len(strs)
        mincol = min([len(x) for x in strs])
        
        while icol < mincol:
            for irow in range(nrow-1):
                if strs[irow][icol] != strs[irow+1][icol]:
                    return pre
            pre += strs[0][icol]
            icol += 1
        
        return pre