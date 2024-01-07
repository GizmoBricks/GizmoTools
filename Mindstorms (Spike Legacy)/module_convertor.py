# Replace `64646` with ID of your module.
with open('/projects/64646/__init__.py', 'r') as file:
    module_name = file.readline().rstrip().split()[1]
    with open('/{}.py'.format(module_name), 'w') as write_file:
        for line in file:
            write_file.write(line)
print('Done')
