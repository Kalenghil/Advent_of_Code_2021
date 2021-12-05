file_name = r'2.txt'
with open(file_name, 'r') as f:
    commands = list(map(lambda x: x.split(), f.readlines()))

aim, x, y = 0, 0, 0
for command in commands:
    type, num = command
    if type == 'forward':
        y += aim * int(num)
        x += int(num)
    elif type == 'down':
        aim += int(num)
    elif type == 'up':
        aim -= int(num)

print(x, y, x * y)
