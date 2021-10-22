def fib(n, m):
    l= [0,1, 1]
    for i in range(3, n + 1):
        if i <= m:

            total = l[i - 1] + l[i - 2]
        elif i == m + 1:

            total = l[i - 1] + l[i - 2] - 1
        else:

            total = l[i - 1] + l[i - 2] - l[i - m - 1]

        l.append(total)
        # print(l)
    return(l[n])
n=int(input("Total month: "))
m=int(input("living month: "))
print(fib(n, m))

