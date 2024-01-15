# Получение ввода от пользователя
user_input = input("Введите элементы списка через запятую: ")

# Проверка и замена возможных разделителей
if ',' in user_input:
    user_input = user_input.replace(',', ' ')
elif ';' in user_input:
    user_input = user_input.replace(';', ' ')
elif '/' in user_input:
    user_input = user_input.replace('/', ' ')

# Разделение ввода на список элементов
numbers = user_input.split()

# Создание нового списка с уникальными элементами
unique_numbers = list(set(numbers))

# Вывод списка с уникальными элементами
print("Результат:", ', '.join(unique_numbers))