#!/usr/bin/python3

import argparse

def gridTravler(row, col, grid=[]):
    grid = [[0 for i in range(col+1)] for j in range(row+1)]

    if grid:
        grid[1][1] = 1

    for r in range(row+1):
        for c in range(col+1):
            current = grid[r][c]
            
            if r+1 <= row:
                grid[r+1][c] =  grid[r+1][c] + current
            if c+1 <= col:
                grid[r][c+1] =  grid[r][c+1] + current

    return grid[r][c]
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--row", type=int)
    parser.add_argument("--col", type=int)

    args = parser.parse_args()
    row,col = args.row,args.col
    
    result = gridTravler(row,col)

    print("A {} by {} grid can be traversed {} ways".format(row, col, result))
    

if __name__ == "__main__":
    main()
