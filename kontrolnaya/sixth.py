from itertools import count


class Cursor:
    # Конструктор, принимающий два параметра - координаты X и Y
    def __init__(self, X, Y):
        self._x = X
        self._y = Y
        self._clicks = list()


    @classmethod
    def our_method(cls):
        print("Hello from class method")


    # Передвинуть по оси X на n и по оси Y на m
    # n, m - произвольные целые числа
    def move(self, n, m):
        self._x += n
        self._y += m

    # Клик в текущем положении курсора
    def click(self):
        self._clicks.append((self._x, self._y))

    # Вернуть количество кликов в заданном прямоугольнике
    def get_click_count(self, min_x, max_x, min_y, max_y):
        return len([None for x, y in self._clicks if min_x <= x <= max_x and min_y <= y <= max_y])


c = Cursor(100, 100)
c.click()
c.move(10, -10)
c.click()
c.move(-10, 10)
c.click()
print(c.get_click_count(95, 105, 95, 105))
print(c.get_click_count(0, 10, 0, 10))

Cursor.our_method()