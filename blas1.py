import sys
def summ(var_1, var_2):
    result = var_1 + var_2 #addition
    return result

def sub(var_1, var_2):
    result = var_1 - var_2 #subtraction
    return result

def mult(var_1, var_2):
    result = var_1 * var_2 #multiplication
    return result

def div(var_1, var_2):
    try:
        result = var_1 // var_2 #division
        return result
    except ZeroDivisionError:
        print("You can't divide by zero !")


def start_1(var_1, var_2, quest):
    var_1 = int(input('Enter your first value: '))
    var_2 = int(input('Enter your second value: '))
    quest = int(input('Choose your calculations by selecting number (example: 1 ): \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division\n '))
    if quest == 1:
          print(summ(var_1, var_2))
    elif quest == 2:
         print(sub(var_1, var_2))
    elif quest == 3:
        print(mult(var_1, var_2))
    elif quest == 4:
        print(float(div(var_1, var_2)))
    else:
         print('Wrong calculation! Please choose from 1 to 4')

def exits(var_1, var_2, quest): #continue to calculate
    while True:
            a = input('Enter yes/no to continue\n').lower()
            if a == 'yes':
                start_1(var_1, var_2, quest)
                continue
            elif a == 'no':
                print('Done! Have a nice day!')
                sys.exit()
            else:
                print('Wrong answer!')
