class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        self.res = 0 
        
        def dfs(index,path):
            lsp, lp = len(set(path)), len(path)
            if lp == lsp:
                self.res = max(self.res, lp)
            if index == n or lp != lsp:
                return
            for i in range(index, n):
                dfs(i + 1, path + arr[i])
        dfs(0, "")
        return self.res