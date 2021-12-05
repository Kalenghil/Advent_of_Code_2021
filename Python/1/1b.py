file_name = r'1a.txt'
with open(file_name, 'r') as f:
    raw_data = list(map(int, f.readlines()))

nums = [sum(raw_data[i:i+3]) for i in range(len(raw_data) - 2)]

counter = 0
for i in range(len(nums) - 1):
    a, b = nums[i:i+2]
    if b > a:
        counter += 1

print(counter)
