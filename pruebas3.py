import os
path = os.path.join(os.path.expanduser('~'), 'Dropbox', 'Reportes', 'file.txt')
print(path)

f = open(path, "a")
f.write("Now the file has more content!")
f.close()