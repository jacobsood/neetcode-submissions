from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # (row, col, min)
        rows, cols = len(grid), len(grid[0])
        queue: deque[tuple[int, int, int]] = deque()
        fresh: int = 0
        minutes = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(rows):
            for col in range(cols):
                cell = grid[row][col]
                if (cell == 1):
                    fresh += 1
                elif (cell == 2):
                    queue.append((row, col, 0))

        while (queue):
            cr, cc, cm = queue.popleft()
            for r, c in dirs:
                nr = cr + r
                nc = cc + c

                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1):
                    continue

                grid[nr][nc] = 2
                queue.append((nr, nc, cm + 1))
                minutes = max(minutes, cm + 1)
                fresh -= 1

        return minutes if fresh == 0 else -1