file_path = r'1a.txt'
with open(file_path, 'r') as f:
    nums = list(map(int, f.readlines()))

counter = 0
for i in range(len(nums) - 1):
    a, b = nums[i:i + 2]
    if b > a:
        counter += 1

print(counter)
