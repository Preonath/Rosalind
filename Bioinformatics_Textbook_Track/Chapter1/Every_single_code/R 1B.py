text=input()
text_len=len(text)
length=int(input())
l=[]
for i in range(text_len-length+1):
    pattern=text[i:i+length]
    l.append(pattern)
s=set(l)
new_dict={i:0 for i in s}
for i in range(text_len-length+1):
    pattern=text[i:i+length]
    new_dict[pattern]=new_dict[pattern]+1
mx=0
for key, val in new_dict.items():
    if(val>mx):
        mx=val
ans=[]
for key, val in new_dict.items():
    if(val==mx):
        ans.append(key)
print(" ".join(ans))


