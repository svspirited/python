string = "tthistorybookrrrrr"

array = list(string)
k = {}

for letter in array:
    if letter in k:
        k[letter] += 1
    else:
        k[letter] = 1

for letter in k:
    if k[letter] > 1:
        print("{} repeated {} times".format(letter, k[letter]))

