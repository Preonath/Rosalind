str1 = '5 1 4 2 3'
numList = str1.split()
numList = list(map(int, numList))
# print(numList)

def inc(s):
    l = [1] * len(s)
    # print(l)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if (s[i] < s[j]):
                l[j] = max(l[j], l[i] + 1)
    print(l)
    a = []
    b = max(l)
    # print(l[::-1])
    for i in l[::-1]: #start : , condition ,  end
        print(l[i])
    #     # print(s[i])
    #     if (b == l[i]):
    #         a.append(s[i])
    #         b = b - 1
    # return a[::-1]
#
f = inc(numList)
# for i in f:
#     print (i, end = ' ')
#
# def dec(s):
#     l = [1] * len(s)
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             if (s[i] > s[j]):
#                 l[j] = max(l[j], l[i] + 1)
#     a = []
#     b = max(l)
#     for i in range(len(s) - 1, -1, -1):
#         if (b == l[i]):
#             a.append(s[i])
#             b = b - 1
#     return a[::-1]
#
# print('\n')
# g = dec(numList)
# for i in g:
#     print (i, end = ' ')
# print('\n')
