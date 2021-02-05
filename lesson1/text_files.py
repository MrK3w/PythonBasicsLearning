#opening file
#/Users/YouUserName/Folder/myfile.txt" for linux
myfile = open("C:\\Temp\\myfile.txt")


#read file
#print(myfile.read())

#get back on the beginning of the file
#myfile.seek(0)
#print("")

#read one line
#print(myfile.readline())

#basic for for reading lines
#myfile.seek(0)
#for line in myfile:
 #   print(line)

#close file
myfile.close()

#w+ reading and writing a+ append 
my_file = open("C:\\Temp\\1.txt",'w+')
my_file.write('This is a new line')
my_file.seek(0)
print(my_file.read())
my_file.close()






