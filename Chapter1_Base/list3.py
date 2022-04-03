import numpy as np


def square(n,list1):
    for value in range(n):
        list1.append(value**2)
    print(list1)

def copy1():
    my_foods = ['pizza','falafel','carrot cake']
    friend_food = my_foods[:]
    my_foods.append('cannoli')
    friend_food.append('ice cream')
    print('revert copy1')
    print(f"my favourite food are {my_foods}")
    print(f"friend's favourite food are {friend_food}")
def copy2():
    my_foods = ['pizza','falafel','carrot cake']
    friend_food = my_foods
    my_foods.append('cannoli')
    friend_food.append('ice cream')
    print('revert copy2')
    print(f"my favourite food are {my_foods}")
    print(f"friend's favourite food are {friend_food}")


if __name__ == '__main__':
    np.random.seed(1)
    # 左闭右开
    a = np.random.randint(0, 100, 200)
    # traverse the list
    for i in a:
        print(i, end=' ')
    print('\n')

    # use range
    for i in range(1, 5):
        print(i, end=' ')
    print('\n')

    # use list(range) to create a list
    numbers = list(range(10))
    print(f"numbers is {numbers}")

    num1 = list(range(0, 21, 2))
    print(f"num1 is {num1}")

    list1 = []
    square(10,list1)

    copy1()
    copy2()


