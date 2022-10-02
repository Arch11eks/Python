import sys
from blas1 import summ, sub, div, mult, exits, start_1


var_1 = int(input('Enter your first value: '))
var_2 = int(input('Enter your second value: '))
quest = int(input('Choose your calculations by selecting number (example: 1 ): \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division\n '))

# print(var1, var2)

if quest == 1:
    print(summ(var_1, var_2))
elif quest == 2:
    print(sub(var_1, var_2))
elif quest == 3:
    print(mult(var_1, var_2))
elif quest == 4:
    print(div(var_1, var_2))
else:
    print('Wrong calculation! Please choose from 1 to 4')

exits(var_1, var_2, quest)
# print(summ())
# print(sub())
# print(mult())
# print(dev())
