f=open('Layer1.png','rb')#read binary
f1=open('MyPic.png','wb')#write binary 

for i in f:
    f1.write(i)