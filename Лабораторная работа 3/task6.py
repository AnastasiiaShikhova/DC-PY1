list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

n = 0
max_ = max(list_numbers)
for i in range(len(list_numbers)):
    if list_numbers[i] == max_:
        n = i
list_numbers[n], list_numbers[-1] = list_numbers[-1], list_numbers[n]

print(list_numbers)
