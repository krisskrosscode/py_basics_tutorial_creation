def read_a_file(filename):
    print('\n\nReading File ...\n\n')
    with open(file=filename, mode='r') as f:
        print(f.read())

def write_to_file(filename):
    print('\n\Wrting to File ...\n\n')
    line = input('Enter the text you want to write : ')
    with open(file=filename, mode='w') as f:
        f.write(line)


def append_to_file(filename):
    print('\n\Appending File ...\n\n')
    line = input('Enter the text you want to write : ')
    with open(file=filename, mode='a') as f:
        f.write(line)

def open_a_file(filename):
    print('\n\Open and read File and then close ...\n\n')
    fileobj = open(file=filename, mode='r')
    print('File is open . Contents of the file : \n', fileobj.read())

    fileobj.close()



open_a_file('p.txt')
read_a_file('p.txt')
append_to_file('p.txt')
write_to_file('p.txt')