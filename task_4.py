# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
# числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо
# обойтись без встроенной функции возведения числа в степень.
while 1:
    try:
        a= int(input("Введите число:"))
        b= int(input("Введите степень:"))
        if b > 0:
            print("Введите отрицательную степень")
        else:
            break
    except:
        print("Степень заданна не верно, введите отрицательную степень")

#Как должно быть
print( a**b )
print(pow(a,b))

#Ответ
def exp_1(a, b):
    res = 1
    b=abs(b)
    for i in range(b):
        res = res*a
    return 1/res

#Рекурсия, ненавижу рекурсии
def exp_2(a, b):
    if b == -1:
        return 1 / a
    p = exp_2(a, b // 2)
    p =p * p
    if b % 2:
        p =p * a
    return p

def exp_3(a,b):
    if b == 0:
        return 1
    else:
        return a * exp_3(a, abs(b) - 1)

print(exp_1(a,b))
print(exp_2(a,b))
print(1/(exp_3(a,b)))