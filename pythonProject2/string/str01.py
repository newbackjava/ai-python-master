data = "감자고구마양파"
print(len(data))
print(data)
print(type(data))
last = data[6] #인덱싱, 슬라이싱
first = data[0]
print('마지막 글자는 %s 첫 글자는 %s' % (last, first))
print('마지막 글자는 {0} 첫 글자는 {1}'.format(last, first))
print('마지막 글자는 {l} 첫 글자는 {f}'.format(l=last, f=first))
our = (last, first) #tuple(readOnly)
print('마지막 글자는 {o[0]} 첫 글자는 {o[1]}'.format(o=our))
print('-------------------')
print(data[0:2]) #0~1
print(data[:2]) #0~1
print(data[2:5])
print(data[5:7])
print(data[5:])

data2 = "생수커피"
data3 = data + data2
print(data3)
