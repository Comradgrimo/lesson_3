# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(a,b,c):
    foo = [a, b, c]
    foo.sort(reverse=True)
    return foo[0]+foo[1]

print(my_func(20,30,40))