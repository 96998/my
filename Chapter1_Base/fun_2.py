# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):  # *topping实际上为一个元组
    print("\nMaking a" + str(size) +
          "-inch pizza with the following topping:")
    for topping in toppings:
        print('- ' + topping)

# 使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

if __name__ == '__main__':
    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
    user_profile = build_profile('alexander','jiajiason',location='China',field='Computer Science')
    print(user_profile)