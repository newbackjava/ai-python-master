#space
s1 = ' samsung'
s2 = '     samsung'
s3 = 'samsung       '
s4 = '    samsung     '
s5 = '    samsung \n\n'

print(s1.lstrip())
print(s2.lstrip())
print(s5.strip())
print(s1.strip() == 'samsung')
# name = input('name>> ')

num_str = ['10','20','30',' 40 ']
for one in num_str:
    if(one.strip() == '40'):
        print('40이 있음.')

# samsung
# samsung
# samsung
# True
# 40이 있음.