file1= open('output.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()

file1= open('output.txt','w')
appending_file = file1.write('Learning file handling in python.')
print(appending_file)
file1.close()

file1= open('output.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()