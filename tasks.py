# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

# numbers=input('Введите число->  ')
# sum_numbers=0
# for i in numbers:
#     try:
#         numbers_s=int(i)
#     except:
#         continue
#     sum_numbers+=numbers_s
# print('Сумма цифр ->',sum_numbers)




# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)






# numbers=input('Введите число->  ')
# fact_numbers=1
# numbers_list=[]
# if numbers.isdigit():
#     numbers=int(numbers)
#     if numbers>=1:
#         for i in range(1,numbers+1):
#             fact_numbers*=i
#             numbers_list.append(fact_numbers)
#     else:
#         print ('число меньше 1')
# else:
#     print('не является числом ->',numbers)
# print('Факториал' ,numbers ,'->',numbers_list)

# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

# numbers=input('Введите значение для проверки полиндрома->  ')
# def find_polindrom(nums):
#     rev_nums=''.join(reversed(nums))
#     if str(nums)==str(rev_nums):
#         return nums+'  is polindrom'
#     return find_polindrom((str(nums)[::-1])+nums)
# print(find_polindrom(numbers))

# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности

import datetime,math
maxd=int(input('input max for random-> '))
mind=int(input('input mix for random->'))
def timerandom_int(mins,maxs):
    diapazon=maxs-mins
    milisec=datetime.datetime.today().microsecond/(10**6)
    
    return mins+math.ceil(diapazon*milisec)
print(timerandom_int(mind,maxd))
