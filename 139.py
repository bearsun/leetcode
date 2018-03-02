# BFS with memory
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        queue = [0]
        visited = []
        n = len(s)
        while queue:
            start = queue.pop(0)
            if start not in visited:
                for i in range(start+1, n+1):
                    if s[start:i] in  wordDict:
                        if i == n:
                            return True
                        queue.append(i)
                visited.append(start)
        return False