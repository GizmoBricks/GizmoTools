ID = 55447 # Replace with ID of your slot with data.

with open('/projects/{}/__init__.py'.format(ID), 'r') as file:
    for line in file:
        print(line)
