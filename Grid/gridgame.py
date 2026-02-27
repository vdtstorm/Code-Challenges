# Find arrow location
def get_arrow(grid):
    arrow = "*"
    found = False
    for i in grid:
        for j in i:
            if j != "*" and j != "@" and j != "#" :
                arrow = j
                found = True
                break
        if found:
            break
    return arrow

def get_row(grid):
    return len(grid)
        
def get_col(grid):
    for i in grid:
        return len(i)
            
            
# Growing the size of the grid
def grow(grid,r,c):
    # If row or col lower than currrent will return current
    if get_col(grid) < c or get_row(grid) < r :
        return grid
    # Fill new grid
    newgrid = fill_grid(r,c)
    # Row,Col of Arrow
    lock = get_location(grid)
    # Assign the location of the arrow in the new grid
    newgrid[lock[0]][lock[1]] = get_arrow(grid)
    
    return newgrid
    
# Prints the grid
def print_grid(grid):
    for cnt,i in enumerate(grid):
        print("".join(i))
    print("\n")

# Fills the grid
def fill_grid(r,c):
    row = []
    col = []
    for i in range(r):
        col = []
        for j in range(c):
            col.append("*")
        row.append(col)
        
    return row

# Finds the location of the arrow
def get_location(grid):
    up = "^"
    down  = "v"
    left = "<"
    right = ">"
    
    r = 0
    c = 0

    found = False
    for row,i in enumerate(grid):
        for col,j in enumerate(i):
            if j == up:
                r = row
                c = col
                found = True
                break
            elif j == down:
                r = row
                c = col
                found = True
                break
            elif j == left:
                r = row
                c = col
                found = True
                break
            elif j == right:
                r = row
                c = col
                found = True
                break
        if found:
            break
    return(r,c)


def turn(grid, direction):
    up = "^"
    down  = "v"
    left = "<"
    right = ">"
    
    lock = get_location(grid)
    
    if direction == "u":
        grid[lock[0]][lock[1]] = up
    elif direction == "d":
        grid[lock[0]][lock[1]] = down
    elif direction == "l":
        grid[lock[0]][lock[1]] = left
    elif direction == "r":
        grid[lock[0]][lock[1]] = right
    
    return grid
        
    
    
    
    

        
row = 10
col = 10

row_col = fill_grid(row,col)




arrow = "<"
r = 1
c = 2

print_grid(row_col)

    
row_col[r][c] = arrow

print_grid(row_col)






row_col = turn(row_col,"r")

print_grid(row_col)


row_col = grow(row_col,15,15)



print_grid(row_col)
