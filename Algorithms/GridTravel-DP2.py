def grid_travel(m, n, blockage):
    grid = [[0 for j in range(n+1)] for i in range(m+1)]
    grid[1][1] = 1
    for block in blockage:
        grid[block[0]][block[1]] = -1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i == j == 1:
                continue
            elif grid[i][j] == -1:
                grid[i][j] = 0
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[m][n]


if __name__ == "__main__":
    m, n = 3, 4
    blockage = [(2,2)]
    print (grid_travel(m, n, blockage))