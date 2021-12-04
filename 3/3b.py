def amount_of_nums_by_digit(nums, len_of_num):
    ans = [0] * len_of_num
    for num in nums:
        for i in range(len_of_num):
            if num[i] == '1':
                ans[i] += 1
            else:
                ans[i] -= 1
    return ans


file_name = r'3.txt'
len_of_num = 12
with open(file_name, 'r') as f:
    nums = f.readlines()

a = amount_of_nums_by_digit(nums, len_of_num)

print(a)


oxygen_generator_rating = nums
for i in range(len_of_num):
    a = amount_of_nums_by_digit(oxygen_generator_rating, len_of_num)
    if len(oxygen_generator_rating) == 2:
        break
    if a[i] > 0:
        oxygen_generator_rating = list(filter(lambda x: x[i] == '1', oxygen_generator_rating))
    else:
        oxygen_generator_rating = list(filter(lambda x: x[i] == '0', oxygen_generator_rating))
    print(oxygen_generator_rating, a, i)
oxygen_generator_rating = int(oxygen_generator_rating[1], 2)

CO2_scrubber_rating = nums
for i in range(len_of_num):
    a = amount_of_nums_by_digit(CO2_scrubber_rating, len_of_num)
    if len(CO2_scrubber_rating) == 2:
        break
    if a[i] > 0:
        CO2_scrubber_rating = list(filter(lambda x: x[i] == '0', CO2_scrubber_rating))
    else:
        CO2_scrubber_rating = list(filter(lambda x: x[i] == '1', CO2_scrubber_rating))
    print(CO2_scrubber_rating, a, i)
CO2_scrubber_rating = int(CO2_scrubber_rating[1], 2)

print(oxygen_generator_rating, CO2_scrubber_rating, oxygen_generator_rating * CO2_scrubber_rating)
