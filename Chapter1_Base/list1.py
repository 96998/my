a = ['1','2','3','4']
print(f"a is {a}")
# append item
a.append('5')
print(f"after append now a is {a}")

# insert item
a.insert(1,'11')
print(f"After insert now a os {a}")

# delete item
del a[1]
print(f"After delete now a is {a}")

# use pop to delete element
b = a.pop()
print(f"b is {b}")
print(f"after pop a is {a}")

# use pop to pop anywhere element
c = a.pop(1)
print(f"c is {c}")
print(f"now a is {a}")

# remove element by value
a.remove('3')
print(f"now after remove a is {a}")

# error! Try to remove a inexistence value
# a.remove('100')

