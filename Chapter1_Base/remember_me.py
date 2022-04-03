import json

filename = './data/name.json'
try:
    with open(filename, 'r') as file1:
        name = json.load(file1)
except FileNotFoundError:
    name = input('What is your name')
    with open(filename, 'w') as file2:
        json.dump(name, file2)
        print("We'll remember you when you come back, " + name + '!')
else:
    print("Welcome back, " + name + '!')
