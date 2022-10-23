# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. 

def change(lst):
    new_start = lst.pop()  # Удаляем последний элемент и сохраняем его в переменную
    new_end = lst.pop(0)  # Удаляем первый элемент и сохраняем его в переменную
    lst.append(new_end)  # Добавляем к списку новый последний элемент
    lst.insert(0, new_start)  # Добавляем к списку новый первый элемент
    return lst


print(change([1, 2, 3]))  # [3, 2, 1]
print(change([1, 2, 3, 4, 5]))  # [5, 2, 3, 4, 1]
print(change(['н', 'л', 'о', 'с']))  # ['с', 'л', 'о', 'н']

#__________________________________________________________

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(change([1, 2, 3]))  # [3, 2, 1]
print(change([1, 2, 3, 4, 5]))  # [5, 2, 3, 4, 1]
print(change(['н', 'л', 'о', 'с']))  # ['с', 'л', 'о', 'н']
