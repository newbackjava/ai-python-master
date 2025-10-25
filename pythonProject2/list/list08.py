#int[][] jumsu = new int[3][2];
jumsu = [
    ['국어',100, ['A+', 'A+']],
    ['수학',85],
    ['영어', 99]
]

jumsu2 = {
    '국어': [100,  ['A+', 'A+']],
    '수학': 85
    }
print(jumsu2.get('국어')[0])
print(jumsu[0][2][1])
str_list = ['100', '200', '300']

int_list = [int(n) for n in str_list]

print(int_list)