src = not False and True or False and not True

result = True and True or False and False # убрали отрицания
result = True or False # убрали "и"
result = True # убрали "или"

print(src == result)
