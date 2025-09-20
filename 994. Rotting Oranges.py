class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            level_size = len(q)
            did_rot_any = False

            for _ in range(level_size):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:

                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
                        did_rot_any = True


            if did_rot_any:
                minutes += 1


        return minutes if fresh == 0 else -1
        
