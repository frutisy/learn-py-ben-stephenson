row = 10
col = 10

for i in range(1, row + 1):
    print(i, end="\t")

    for j in range(1, col + 1):
        print(i * j, end="\t")

    print()
