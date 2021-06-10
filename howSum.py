
import argparse

def howSum(m, n, possible=[]):
    if m == 0:
        return []
    if m < 0:
        return None
    
    for num in n:
        remainder = m - num
        remainderResult = howSum(remainder, n, possible)

        if remainderResult != None:
            possible.append(num)
            return possible

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
