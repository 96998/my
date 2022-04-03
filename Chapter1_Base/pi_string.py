filename = './data/pi_million_digits.txt'
with open(filename) as file1:
    lines = file1.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(f"The length of pi is {len(pi_string)}")
print(pi_string[:52])
# 检查生日是否在其中
bir = '19990405'
if bir in pi_string:
    print('Your birth in pi')
else:
    print('Pi do not include birth')

