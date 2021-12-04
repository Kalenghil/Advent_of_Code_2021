file_name = r'2.txt'
with open(file_name, 'r') as f:
    commands = list(map(lambda x: x.split(), f.readlines()))

x, y = 0, 0
for command in commands:
    type, num = command
    if type == 'forward':
        x += int(num)
    elif type == 'down':
        y += int(num)
    elif type == 'up':
        y -= int(num)

print(x, y, x * y)
