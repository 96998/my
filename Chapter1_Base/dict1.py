from collections import OrderedDict

languanges = OrderedDict()
languanges['jen'] = 'Python'
languanges['sarah'] = 'C'

for name,lan in languanges.items():
    print(name.title()+" 's favourite language is "+
          lan.title()+".")