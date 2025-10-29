import ast
import copy

x = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
y = copy.deepcopy(x);

print("x =", x)
print("y =", y)
print("----------")
y[0][0] =  100
print("x =", x)
print("y =", y)

print("=====================")
x2 = {1 : [1,2,3], 2 : 2}
y2 = copy.deepcopy(x2);
y2[1][0] = 100
print("x2 =", x2)
print("y2 =", y2)

names = "{1 : 1, 2 : 2, 3 : 3}"
json_names = ast.literal_eval(names)
print("json_names =", type(json_names))

