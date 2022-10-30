def get_count_char(str_):
    str_ = str_.lower()
    str_ = ''.join(str_.split())
    dict_counts = {}

    for i in range(len(str_)):
        if str_[i].isalpha() == True:
            if str_[i] in dict_counts:
                dict_counts[str_[i]] += 1
            else:
                dict_counts[str_[i]] = 1

    return dict_counts



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
