start, end = input('시작, 끝값 입력>>').split(',')
start2 = int(start)
end2 = int(end)
print(start2)
print(end2)
#[1,2,3,4,5]
length = len(list(range(start2, end2 + 1)))
print('개수는 ', length)

sum = 0
for x in range(start2, end2 + 1):
    sum += x
print('sum: %d점' % sum )
print('avg: %0.1f' % (sum / length))

print('--------')

sum = 0
for n in range(10, 21):
    sum += n
print(sum)
