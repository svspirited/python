import argparse
from iteration_utilities import deepflatten
#
# Recursively cycle through a list of string fragments
# to determine if the target string can be constructed
# using available segments, any segment can be used multiple
# times to acheive this and return the boolean result
#

def howConstruct(target, stringBank):
    if target == '':
        return [[]]

    result = []
    
    for word in stringBank:
        if word in target:
            if target.index(word) == 0:
                suffix = target[len(word):]
                suffixWays = howConstruct(suffix, stringBank)
                targetResults = list(deepflatten([word, suffixWays], ignore=str))

                if len(list(deepflatten(targetResults))) >= len(target):
                    result.append(targetResults)

    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", type=str)
    parser.add_argument("--words", type=str, nargs='+')

    args = parser.parse_args()

    m = args.word
    n = args.words

    result = howConstruct(m,n)
    
    if result == []:
        print("{} can not be built with any combination in {}".format(m,n))
    else:
        print(result)
    
if __name__ == "__main__":
    main()
