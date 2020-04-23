import os

os.path.getsize('C:\\Af\\pr.exe')  # returns the size in bytes of the file
os.listdir('C:\\Af')  # returns the file names within a folder ['a.txt','b.txt','c.txt']
os.path.exists('C:\\Windows')  # returns True if the path exists
os.path.isfile('C:\\Af\\pr.exe')  #returns True - this is a file
os.path.isfile('C:\\Af')  #returns False - this is not a file
os.path.isdir('C:\\Af')  #returns True - this is a directory
os.path.isdir('C:\\Af\\pr.exe')  #returns False - this is not a directory
