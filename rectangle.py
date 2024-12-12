def area(a, b):
    """
        возвращает площадь прямоугольника
        a(int) - длина
        b(int) - ширина
        возвращаемое значение: a * b - искомая площадь
    """
    if type(a) is not int and type(b) is not int:
        raise TypeError("аргументы должны быть int")
    if a<= 0 or b<= 0:
        raise ValueError("аргументы должны быть > 0")

    return a * b

def perimeter(a, b):
    """
            возвращает периметр прямоугольника
            a(int) - длина
            b(int) - ширина
            возвращаемое значение: a * b - искомая периметр
        """
    if type(a) is not int and type(b) is not int:
        raise TypeError("аргументы должны быть int")
    if a<= 0 or b<= 0:
        raise ValueError("аргументы должны быть > 0")

    return 2*(a + b)
