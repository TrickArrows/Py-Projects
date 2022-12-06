filename = 'text.txt';
#write
print(open(filename,'w').write("Hello World\n"))

#read
print(open(filename,'r').readlines())

#append
print(open(filename,'a').write("python3\n"))



#read the lines after added
print(open(filename,'r').readlines())
