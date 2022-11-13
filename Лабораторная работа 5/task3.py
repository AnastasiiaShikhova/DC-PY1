from random import randint

def get_unique_list_numbers(begin = -10, end = 10, count = 15) -> list[int]:
    not_unique_list = [randint(begin, end) for i in range(count)]
    future_unique_list = list(set(not_unique_list))

    while len(future_unique_list) != len(not_unique_list):
        future_unique_list = future_unique_list + [randint(begin, end)]
        future_unique_list = list(set(future_unique_list))

    return future_unique_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

