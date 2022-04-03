import numpy as np

a = np.random.randint(1, 100, 20)
a = a.tolist()
# Do not change a
b = sorted(a)
print(f"a is {a}")
print(f"b is {b}")
# Change a
a.sort()
print(f'Now a is {a}')
# Reverse the value of a
a.sort(reverse=True)
print(f"reverse is {a}")

cars = ['bmw', 'audi', 'toyata', 'subaru']
print(cars)
# reverse()不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排
# 列顺序
cars.reverse()
print(cars)

# print the len of list
print(f"The length of a is {len(a)}")
