text = input()
len_text = len(text)
pattern = input()
len_pattern = len(pattern)
cnt = 0
for i in range(0, len_text):
    match = text[i:i + len_pattern]
    if match == pattern:
        cnt = cnt + 1

print(cnt)