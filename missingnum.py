a = [1,2,4,5,7,8,10]
a1 = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(a)):
    c = a[i]+1
    print(c, i)
    if (( i + 1 ) == c):
        print(c)

