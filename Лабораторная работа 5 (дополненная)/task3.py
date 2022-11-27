from random import randint

def get_unique_list_numbers(begin = -10, end = 10, count = 15) -> list[int]:
    if (begin > end):
        raise ValueError('Некорректные границы')
    elif ((abs(begin) + abs(end)) < count):
        raise ValueError('Некорректное количество')
    else:
        unique_list = []
        while len(unique_list) != count:
            number = randint(begin, end)
            if number not in unique_list:
                unique_list.append(number)
    return unique_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

