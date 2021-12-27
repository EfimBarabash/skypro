# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    speed = 1

    def __init__(self, coord_x, coord_y, field):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.field = field
        self.state = 'crawl'

    def change_state(self):
        if self.state == 'crawl':
            self.state = 'fly'
        else:
            self.state = 'crawl'


    def get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        return self.speed * 0.5


    def move(self, direction):
        speed = self.get_speed()
        if direction == 'UP':
            new_y = self.coord_y + speed
        elif direction == 'DOWN':
            new_y = self.coord_y - speed
        elif direction == 'LEFT':
            new_x = self.coord_x - speed
        elif direction == 'RIGTH':
            new_x = self.coord_x + speed

            self.field.set_unit(x=self.coord_x, y=self.coord_y, unit=self)

#     ...
