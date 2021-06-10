
def  howSum(m, n, possible=[]):
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
    m = 1024
    n = [50, 40, 13, 26, 4, 3, 12, 8]

    sums = howSum(m, n)

    print("sum of {} = {}".format(sums, sum(sums)))
    
    pass

if __name__ == "__main__":
    main()
