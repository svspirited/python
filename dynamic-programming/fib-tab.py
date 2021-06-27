#!/usr/bin/python3

import argparse

def fib(num):
    nums = []
    for n in range(0, num+1):
        nums.append(0)

    nums[1] = 1
    
    for n in range(len(nums)):
        if n <= (num-2):
            nums[n+1] = nums[n+1] + nums[n]
            nums[n+2] = nums[n+2] + nums[n]
        elif n <= (num-1):
            nums[n+1] = nums[n+1] + nums[n]

    return(nums[n])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int)

    args = parser.parse_args()

    num = args.num
    
    num = fib(num)
    print(num)

if __name__ == "__main__":
    main()
        
