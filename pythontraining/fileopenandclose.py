file=open("sample.txt","w")   #open file in write mode
file.write("Hello,this is sample text ")     #write data
file.write("Hey")
file.close()            #close the file

#reading the entire file
with open("sample.txt","r") as file:
    content=file.read()
    print(content)

#reading line by line
with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())
        