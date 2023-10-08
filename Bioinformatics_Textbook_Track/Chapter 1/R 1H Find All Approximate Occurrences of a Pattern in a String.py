ans = list()


def patternmatch(pattern, text, d):
    L = len(text)
    L2 = len(pattern)
    for i in range(L - L2 + 1):
        cnt = 0
        for j in range(L2):
            if text[i + j] != pattern[j]:
                cnt += 1
        if cnt <= d:
            ans.append(i)


pattern = input("Input the pattern: ")
text = input("Input the text: ")
d = int(input())

patternmatch(pattern, text, d)

print(*ans)