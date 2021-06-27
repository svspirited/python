#!/usr/bin/python3

# from functools import lru_cache

# @lru_cache
def gridPaths(m, n, memo={}):
    
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    key = (m,n)
    if key in memo:
        return memo[key]
    
    memo[key] = gridPaths(m - 1, n, memo) + gridPaths(m, n -1, memo)
    return memo[key]
    
def main():
    print(gridPaths(1,1))
    print(gridPaths(0,1))
    print(gridPaths(18,18))
    print(gridPaths(100,100))
    
    pass

if __name__ == "__main__":
    main()
    
