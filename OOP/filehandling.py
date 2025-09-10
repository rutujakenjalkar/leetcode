
import os
#two types of path :
""" relative :path specific to directory
absolute path:from root to file entire list of directories"""

#access modes:
"""
always ass them in double quotes
r,w,a,r+(read+write),a+(append,read),w+(write,read)
bianry format:
rb,wb,ab,rb+,wb+,ab+
always add them in double quotes

w,wb overried the file contents while writing 
"""

#opening a file:
file1=open("C:\\Users\\Abhay\\Documents\\internimage\\meetingnotes.txt","r")
print(file1)

#to check access mode 
print(file1.mode)

#to check if file is open or closed if closed =tru else false
print(file1.closed)

#to check name of file -gives fiel path
print(file1.name)

# you can open only some files for a prog no infite

#to close a file
#file1.close()
#print(file1.closed)

#WRITE METHOD IS USED TO WRITE IN A FILE PUT NOT ALWAYS ON A NEW LINE(also return none value)
#file1.write("this is the end")

#writelines method to write multiple lines or list of string
#list1=['a','b']
#file1.writelines(list1)

#read ()-to read the contents of the file from beginning
""" if arg no val or -ve val then entire cotents read
if arg val is psecified it is the number of bytes to read
return \n new line character"""

#print(file1.read())

#readline method to read line from the txt. first readline starts executing from 1st line next time it is excuteed control goes to the ext 
#line

# splitting line if no chracter  mentioned then space otherwise mentioned character ued for splitting
#line =file1.readline()
#rye=line.split()
#print(rye)
#print(file1.readline())
#prints nothing of empty line

#readlines to read all llnes in the file
#print(list(file1))
# file1.readlines()-empty string if pointer already at end

#filepointer
print(file1.tell())
#offest to tell psotion from with to carryout operation set pointer to loaction
"""
0-start if file
1-current pos in file
2-end of file"""

# eg file1.seek(5,0) from start pos 5 space
# file1.seek(4,2) 4th pos from end

"""rename the file"""
#os.rename("C:\\Users\\Abhay\\Documents\\internimage\\meetingnotes.txt","C:\\Users\\Abhay\\Documents\\internimage\\notes.txt")
""" remove the file"""
#os.remove ("C:\\Users\\Abhay\\Documents\\internimage\\meetingnotes.txt")

#to make dorectory
#os.mkdir("rutuja")
#print("created")

print(os.getcwd())

#os.chdir("")
print(os.getcwd())
os.rmdir("aplha")

#os.mkdirs("c:\\a1\\a2\\sw\\s3") -- crete multiple directories if if a1 and a2 exist then create sw and s3
