text = input("input the text: ")
len_text = len(text)
length = int(input("input particular length: "))

lst = []
for i in range(len_text - length + 1):
    pattern = text[i:i + length]
    lst.append(pattern)

# print (lst)
lst = set(lst)
# print (lst)

new_dict = {i: 0 for i in lst}
# print(new_dict)

for i in range(len_text - length + 1):
    pattern = text[i:i + length]
    # print(pattern)
    new_dict[pattern] = new_dict[pattern] + 1
# print(new_dict)
mx = 0
for str1, val in new_dict.items():
    if mx < val:
        mx = val
        # my_str = str1
# print(mx)
ans = []
for str1, val in new_dict.items():
    if mx == val:
        # my_str = str1
        ans.append(str1)

print(" ".join(ans))