# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def my_func (name, sename,year, city, email, phone_number):
    return (f'Данные о пользователе - Имя: {name} Фамилия: {sename} Год Рождения: {year} Город проживания: {city} '
            f'Email: {email} Телефон: {phone_number}')

print(my_func("Иван","Иванов","01.01.1920","Москва","ivanoff@mail.ru","88005553535"))