def get_count_char(str_):
    str_ = str_.lower()
    dict_counts = {}

    for symbol in str_:
        if symbol.isalpha():
            dict_counts[symbol] = dict_counts.get(symbol, 0) + 1

    return dict_counts

def percent_of_symbols(dict_w_symbols):
    dict_w_percent = {}
    part = 100 / sum(dict_w_symbols.values())

    for key in dict_w_symbols:
        dict_w_percent[key] = round(dict_w_symbols.get(key) * part, 2)

    return dict_w_percent

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print()
print(percent_of_symbols(get_count_char(main_str)))
