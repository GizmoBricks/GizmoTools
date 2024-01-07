with open('/flash/program/00/program.mpy', 'br') as file:
    next(file)
    module_name = str(file.readline().rstrip().split()[1], 'UTF-8')
    with open('/flash/{}.py'.format(module_name), 'w') as write_file:
        
        for line in file:
            try:
                write_file.write(str(line, 'UTF-8'))
            except UnicodeError:
                break
print('Done')
