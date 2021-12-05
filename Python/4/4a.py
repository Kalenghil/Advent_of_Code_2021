import pprint
import re


def check(rows):
    len_of_table = len(rows)
    win = ['*', '*', '*', '*', '*']
    columns = list(zip(*rows))
    if (any(column == win for column in columns) or
            any(row == win for row in rows)):
        return True

    fst_diagonal = [rows[i][i] for i in range(len_of_table)]
    snd_diagonal = [rows[len_of_table - 1 - i][len_of_table - 1 - i] for i in range(len_of_table)]

    if snd_diagonal == win or fst_diagonal == win:
        return True
    return False


def fill(rows, num):
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == num:
                rows[i][j] = '*'

def sum_of_table():
    pass


file_path = r'4.txt'
with open(file_path, 'r') as f:
    moves = f.readline().split(',')
    raw_data = list(map(lambda x: x.strip(), f.readlines()))

tables = list()
table = list()
for line in raw_data[1:]:
    if line == '':
        tables.append(table)
        table.clear()
    else:
        table.append(re.split(r'\s+', line))

flag = True
for move in moves:
    if flag:
        for table in tables:
            fill(table, move)
            if check(table):
                flag = False
                win_move = move
                win_table = table
                break

print(win_table)
print(win_move)

summ = 0
for row in win_table:
    for elem in row:
        if elem != '*':
            summ += int(elem)
print(summ)
print(summ * int(win_move))