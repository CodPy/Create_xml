filevar = open('log.txt','r')
ftext=filevar.read()
print (ftext)
new=ftext.replace('строка 333',"меня_поменяли")
print (new)
f1=open ('newfile.txt','w')
f1.write(new)
f1.close()
filevar.close()
