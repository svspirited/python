
import argparse

def howSum(m, n, memo={}, possible=[]):
    if m in memo:
        return memo[m]
    if m == 0:
        return []
    if m < 0:
        return None
    
    for num in n:
        remainder = m - num
        memo[m] = possible
        remainderResult = howSum(remainder, n, memo, possible)
        
        if remainderResult != None:
            possible.append(num)
            memo[m] = possible
            return possible

    memo[m] = None
    return None
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", type=int)
    parser.add_argument("--numbers", type=int, nargs='+')

    args = parser.parse_args()

    m = args.number
    n = args.numbers

    sums = howSum(m, n)

    if sums:
        print("sum of {} = {}".format(sums, sum(sums)))
    else:
        print("No combination in {} adds to {}".format(n,m))

if __name__ == "__main__":
    main()
