import random

from work import Worker

gender_list = ['남', '여']
if __name__ == '__main__':
    for index in range(1000):
        age_rand = random.randint(20, 35)
        gender_choice = random.choice(gender_list)
        Worker('홍길동'+str(index), age_rand, gender_choice)
        print('채용인원>> ', Worker.count)

    w1 = Worker('홍길동', 25, '남')
    print('채용인원>> ', Worker.count)

    w2 = Worker('김길동', 23, '여')
    print('채용인원>> ', Worker.count)

    w3 = Worker('박길동', 28, '남')
    print('채용인원>> ', Worker.count)

    w4 = Worker('이길동', 21, '남')
    print('채용인원>> ', Worker.count)

    w5 = Worker('장길동', 29, '여')
    print('채용인원>> ', Worker.count)

    print(w1)
    print(w2)
    print(w3)
    print(w4)
    print(w5)
    print(Worker.age_sum)
    print(Worker.count)
    print(Worker.age_sum//Worker.count)
    print('남자 직원수 >> ', Worker.m)
    print('여자 직원수 >> ', Worker.f)