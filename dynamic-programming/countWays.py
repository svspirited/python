import argparse

#
# Recursively cycle through a list of string fragments
# to determine if the target string can be constructed
# using available segments, any segment can be used multiple
# times to acheive this and return the boolean result count
# how many times this can be done
#

def countBuild(target, stringBank, results=[], memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return 1

    totalWays = 0
    
    for word in stringBank:
        if word in target:
            if target.index(word) == 0:
                suffix = target[len(word):]
                ways = countBuild(suffix, stringBank, results, memo)
                totalWays = totalWays + ways

    memo[target] = totalWays
    return totalWays

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", type=str)
    parser.add_argument("--words", type=str, nargs='+')

    args = parser.parse_args()

    m = args.word
    n = args.words

    result = countBuild(m,n)
    if result == []:
        print("{} can not be built with any combination in {}".format(m,n))
    else:
        print(result)
    
if __name__ == "__main__":
    main()
