"""
Напишите программу для ввода строки
и выведите её с обратным порядком следования символов в словах.
В решении задачи готовых методов использовать не буду
"""

def reverse_string(string):
    reversed_string = ""
    length = len(string)
    symbols_of_reversed_string = [""] * length
    index = len(symbols_of_reversed_string) - 1
    for symbol in string:
        symbols_of_reversed_string[index] = symbol
        index -= 1
    for symbol in symbols_of_reversed_string:
        reversed_string += symbol
    return reversed_string


if __name__ == '__main__':
    original_string = input("Enter a string: ")
    print("Исходная строка: ", original_string)
    string_by_end = reverse_string(original_string)
    print("Перевернутая строка: ", string_by_end)