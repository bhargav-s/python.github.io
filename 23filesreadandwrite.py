fw = open('sample.txt','w')
fw.write("Hey how are you")
fw.close()

fr = open('sample.txt','r')
tr = fr.read()
print(tr)
fr.close()