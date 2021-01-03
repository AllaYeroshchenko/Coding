# 200. Number of Islands


def numIslands(grid):
    global islands
    islands=0
    n=len(grid)
    m=len(grid[0])
    q = sum([int(grid[i][j]) for i in range(n) for j in range(m)]) 
    if q == 0:
        return 0
    def find_island(grid):
        global islands
        i=j=0
        flag=False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    print(i, j)
                    islands+=1
                    flag = True
                    break 
            if flag == True:
                break
            
        def addnode(i, j, grid):
            grid[i][j] = "0"
            if i+1 < n and grid[i+1][j] == "1":
                addnode(i+1, j, grid)
            if j+1 < m and grid[i][j+1] == "1":
                addnode(i, j+1, grid)
            if i-1 >= 0 and grid[i-1][j] == "1":
                addnode(i-1, j, grid)
            if j-1 >= 0 and grid[i][j-1] == "1":
                addnode(i, j-1, grid)

        addnode(i, j, grid)
        

    while True:
        q = sum([int(grid[i][j]) for i in range(n) for j in range(m)]) 
        if q > 0:
            find_island(grid)
            print(grid)
            print(islands)
        else:
            return islands



'''grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","1"],
        ["0","0","0","1","1"]]
'''
grid = [["1","0","1","1","0","1","1"]]

islands=0

print(numIslands(grid))



"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islands=0
        n=len(grid)
        m=len(grid[0])
        q = sum([int(grid[i][j]) for i in range(n) for j in range(m)]) 
        if q == 0:
            return 0
        def find_island(grid):
            i=j=0
            flag=False
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == "1":
                        self.islands+=1
                        flag = True
                        break 
                if flag == True:
                    break
            
            def addnode(i, j, grid):
                grid[i][j] = "0"
                if i+1 < n and grid[i+1][j] == "1":
                    addnode(i+1, j, grid)
                if j+1 < m and grid[i][j+1] == "1":
                    addnode(i, j+1, grid)
                if i-1 >= 0 and grid[i-1][j] == "1":
                    addnode(i-1, j, grid)
                if j-1 >= 0 and grid[i][j-1] == "1":
                    addnode(i, j-1, grid)

            addnode(i, j, grid)
        
        while q > 0:
            q = sum([int(grid[i][j]) for i in range(n) for j in range(m)]) 
            if q > 0:
                find_island(grid)
            else:
                return self.islands

"""