file_name = r'3.txt'
a = [0] * 12
with open(file_name, 'r') as f:
    nums = f.readlines()

for num in nums:
    for i in range(12):
        if num[i] == '1':
            a[i] += 1
        else:
            a[i] -= 1

print(a)

max_num = ''
for i in a:
    if i > 0:
        max_num += '1'
    else:
        max_num += '0'
max_num = int(max_num, 2)
min_num = 4095 - max_num

print(max_num, min_num, max_num * min_num)
print(bin(max_num), bin(min_num))
