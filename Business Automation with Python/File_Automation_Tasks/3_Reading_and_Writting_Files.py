myfile = open('C:\\Af\\hello.txt', 'r')  # opens file in read mode
myfile.read()  # reads the full content of the file
myfile.readlines()  # reads all the content, line by line
myfile = open('C:\\Af\\hello.txt', 'w')  # opens the file in write mode (overwrites any existing content)

myfile.write('writting new content...')  # writes a string contents to the file
myfile.close()  # closes the file for reading/writting
myfile = open('C:\\Af\\hello.txt', 'a')  # opens file in append mode
myfile.write('appending new content...')  # appends extra content to an existing file

# write(no new character)  #write doens't add the newline character
