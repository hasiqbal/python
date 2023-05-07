# return the number of character in the file 

file = open('name-list-app/day6/essay.txt','r')
content = file.read()
length = len(content)
print(length)