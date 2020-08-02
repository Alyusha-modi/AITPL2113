import os

#This function gives the name of the operating system dependent module imported.
print(os.name)

#returns the Current Working Directory
print(os.getcwd())

## To print absolute path on your system
print(os.path.abspath('.'))

# To print files and directories in the current directory on your system
print(os.listdir('.'))

try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'GFG.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()

# Control jumps directly to here if
# any of the above lines throws IOError.
except IOError:

    # print(os.error) will <class 'OSError'>
    print('Problem reading: ' + filename)

    fd = "GFG.txt"
    # popen() is similar to open()
    file = open(fd, 'w')
    file.write("Hello")
    file.close()
    file = open(fd, 'r')
    text = file.read()
    print(text)

    # popen() provides a pipe/gateway and accesses the file directly
    file = os.popen(fd, 'w')
    file.write("Hello")
    # File not closed, shown in next function

    fd = "GFG.txt"
    os.rename(fd, 'New.txt')

