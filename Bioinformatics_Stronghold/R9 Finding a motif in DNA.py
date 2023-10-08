def sub_string(str,sub):

    position=[]
    for i in range(0,len(str)-len(sub)):
        match=str[i:i+len(sub)]
        if match==sub:]
    return(position)

DNA=input()
motif=input()
print(*sub_string(DNA,motif))