def fi():
    f=open("file3c.txt", "r")
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].strip()
    return(data)
def sp(k):
 a=k[0]
 for i in range(len(k)):
     a+=k[i][(len(k)-1)]
 return a
if __name__ =="__main__":
     k=fi()
     print(sp(k))
