s = str(input())

mn = 123434232
cnt = 0
lst = list()
lst2 = list()

for x in s:
  if x=='G':
    cnt = cnt + 1
  if x=='C':
    cnt = cnt - 1
  lst.append(cnt)
  if mn>cnt:
    mn = cnt

index = 1
for x in lst:
  if x==mn:
    lst2.append(index)
  index = index + 1

for i in lst2:
    print(i, end=" ")