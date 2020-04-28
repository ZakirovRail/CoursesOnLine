import shutil, os

os.chdir('C:\\')  # changes the current working folder

shutil.copy('C:\\file.txt', 'C:\\new')  # copies file.txt to C:\new

shutil.copy('/file.txt', './file2.txt')  # copies file.txt to file2.txt

shutil.copytree('C:\\old', 'C:\\new2')  # copies full content of old to new2

shutil.move('C:\\file.txt', 'C:\\new2')  # moves file.txt to new2

os.unlink('C:\\file.txt')  # permanently removes file.txt

os.rmdir('C:\\new2')  # permanently removes the new2 folder

shutil.rmtree('C:\\new2')  # permanently removes new2 and all in it
