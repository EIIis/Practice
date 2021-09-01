class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        seen = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    if (i, j) in seen:
                        continue
                    else:
                        count += 1
                        self.DFS(grid, i, j, seen)

        return count                   
                        
    def DFS(self, grid, i, j, seen):
        if (i, j) in seen:
            return
        elif i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        elif grid[i][j] == "1":
            seen.add((i, j))
            self.DFS(grid, i+1, j, seen)
            self.DFS(grid, i, j+1, seen)
            self.DFS(grid, i-1, j, seen)
            self.DFS(grid, i, j-1, seen)
                         