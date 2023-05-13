#Write a program in Python to implement readline, readlines, write line and writelines
#file handling mechanisms.
#readline
f=open("vasu.txt","r")
print(f.readline())
#f.close()
#readlines
f=open("vasu.txt","r")
print(f.readlines())
#f.close()
#write line
f=open("vasu.txt","w")
f.write("hello prashant how are you")
#f.close()
#write lines
f=open("vasu123.txt","w")
f.writelines("hello prashant how are you\n i am fine thank you and you \n i am also fine")
f.close()
