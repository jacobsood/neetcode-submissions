from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # (row, col, min)
        rows, cols = len(grid), len(grid[0])
        queue: deque[tuple[int, int]] = deque()
        fresh: int = 0
        minutes = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(rows):
            for col in range(cols):
                cell = grid[row][col]
                if cell == 1:
                    fresh += 1
                elif cell == 2:
                    queue.append((row, col))

        while queue and fresh > 0:
            # go level by level
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
                        
            minutes += 1

        return minutes if fresh == 0 else -1