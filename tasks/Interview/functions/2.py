# Задача:
# Чтобы проверить понимание параметров и область их видимости, Николай создал 3 функции (представлены ниже). 
# Попытайтесь предугадать, как поведет себя каждая из них при запуске (возникнут ли ошибки, что возвратится).
 
def func1():
    param = 4
 
    def inner():
        param += 1
 
    return param
 
 
def func2():
    param = 4
 
    def inner(var):
        var += 1
 
    inner(param)
    return param
 
 
def func3():
    param = 4
 
    def inner(var):
        var += 1
        return var
 
    param = inner(param)
    return param

print(func1())  # 4
print(func2())  # 4
print(func3())  # 5

# Решение:
# Ошибок нет, попробуем разобраться в каждом представленном случае.
# 1) Первая функция
# Во внутренней функции мы пытаемся воспользоваться внешней переменной. Но она не доступна. Ошибки не возникло по единственной причине: мы эту функцию не вызвали.
# 2) Вторая функция
# Внутренняя функция увеличила значение переменной на 1, но сама она ничего не возвращает (кроме None), поэтому значение param не поменялось.
# 3) Третья функция
# В данном случае вернулось 5, так как мы во внутренней функции увеличили внешнюю переменную и присвоили результат в func3.
