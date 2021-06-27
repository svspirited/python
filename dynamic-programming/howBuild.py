import argparse

#
# Recursively cycle through a list of string fragments
# to determine if the target string can be constructed
# using available segments, any segment can be used multiple
# times to acheive this and return the fragments that
# allow for the construction of the string
#
def howBuild(target, stringBank, results=[]):
    if target in results:
        return True
    if target == '':
        return True
    
    for word in stringBank:
        if word in target:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if howBuild(suffix, stringBank):
                    results.append(word)
                    return results
                
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", type=str)
    parser.add_argument("--words", type=str, nargs='+')

    args = parser.parse_args()

    m = args.word
    n = args.words

    result = howBuild(m,n)
    if result == []:
        print("{} can not be built with any combination in {}".format(m,n))
    else:
        print(result)
    
if __name__ == "__main__":
    main()
