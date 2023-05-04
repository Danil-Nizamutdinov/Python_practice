# Создаем словарь соответствия римских цифр и их значений
roman_dict = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}

# Входная римская цифра
roman_num = 'XIV'

# Инициализируем результат
result = 0
i = 0

# Идем по цифрам входной римской цифры
while i < len(roman_num):
    # Если символ парсится как одна римская цифра
    if i == len(roman_num) - 1 or roman_dict[roman_num[i]] >= roman_dict[
            roman_num[i + 1]]:
        result += roman_dict[roman_num[i]]
        i += 1
    else:  # Иначе, парсим как две римские цифры
        result += roman_dict[roman_num[i + 1]] - roman_dict[roman_num[i]]
        i += 2  # здесь мы перескакиваем через 2 римские цифры

# Выводим результат
print(result)  # 14
