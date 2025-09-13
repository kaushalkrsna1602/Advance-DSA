def orangesRotting(grid):
        m = len(grid)
        n = len(grid[0])
        queue = []
        # add all rotten into the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j , 0])
        maxMinutes = 0
        while len(queue):
            [x,y,level] = queue.pop(0)
            if x > 0 and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                queue.append([x-1, y, level+1])
            if x < m-1 and grid[x+1][y] == 1:
                grid[x+1][y] = 2
                queue.append([x+1, y, level+1])
            if y < n -1 and grid[x][y + 1] == 1:
                grid[x][y+1] = 2
                queue.append([x, y+1, level+1])
            if y > 0 and grid[x][y - 1] == 1:
                grid[x][y-1] = 2
                queue.append([x, y-1, level+1])
            maxMinutes = max(level , maxMinutes)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return maxMinutes
            

print(orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))