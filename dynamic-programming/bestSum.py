import argparse
import copy

#
# Recursively  look to find the best combination
# to add up to m
#
def bestSum(m, n, combination=[], memo={}):
    if m == 0:
        return []
    if m in memo:
        return memo[m]
    if m < 0:
        return None

    shortestCombination = []
    
    for num in n:
        remainder = m - num
        remainderCombination = bestSum(remainder, n, combination, memo)

        if remainderCombination != None:
            combination = copy.deepcopy(remainderCombination)
            combination.append(num)
            
            if len(shortestCombination) == 0 or len(combination) < len(shortestCombination):
                shortestCombination = combination
                memo[m] = shortestCombination
                combination = None

    if sum(shortestCombination) == m:
        memo[m] = shortestCombination        
        return memo[m]

    return None
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", type=int)
    parser.add_argument("--numbers", type=int, nargs='+')

    args = parser.parse_args()

    m = args.number
    n = args.numbers
    
    n.sort(reverse=True) # Try the largest numbers first to avoid max recursion error
    sums = bestSum(m, n)

    if sums:
        print("sum of {} = {}".format(sums, sum(sums)))
    else:
        print("No combination in {} adds to {}".format(n,m))

if __name__ == "__main__":
    main()
