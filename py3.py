# to read and write in a file
fw=open('py3.txt','w')
fw.write('my name is charul')
fw.close()

fr=open('py3.txt','r')
print(fr.read())
fr.close()
