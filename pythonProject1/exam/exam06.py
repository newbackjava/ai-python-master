# 상수로 선언
JJ_PRICE = 4500
JB_PRICE = 3000

# 순차문 : 입력 --> 처리 --> 출력
jj_order = int(input("자장면 주문 수 >> "))
jb_order = int(input("짬뽕 주문 수 >> "))

jj_total = jj_order * JJ_PRICE;
jb_total = jb_order * JB_PRICE;
food_total = jj_total + jb_total;

print("자장면 금액 ", jj_total);
print("짬뽕 금액 ", jb_total);
print("전체 주문 금액 ", food_total);
