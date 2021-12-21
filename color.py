from abc import ABC, abstractmethod


class ComputerColor(ABC):

    @abstractmethod
    def __repr__(self):
        return

    @abstractmethod
    def __mul__(self, other):
        return

    @abstractmethod
    def __rmul__(self, other):
        return


class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __str__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other):
        if isinstance(other, Color):
            if other.red == self.red and other.green == self.green and other.blue == self.blue:
                return True
            else:
                return False
        else:
            print('Other does not belong to Color class')

    def __add__(self, other):
        resulting_red = (self.red + other.red) // 2
        resulting_green = (self.green + other.green) // 2
        resulting_blue = (self.blue + other.blue) // 2
        return Color(resulting_red, resulting_green, resulting_blue)

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, other: float):
        contrast_level = -256 * (1 - other)
        contrast_correction = 259 * (contrast_level + 255) / (255 * (259 - contrast_level))

        if other < 0 or other > 1:
            raise ValueError('Contrast multiplicator must be between 0 and 1')
        else:
            new_red = int(contrast_correction * (self.red - 128) + 128)
            new_green = int(contrast_correction * (self.green - 128) + 128)
            new_blue = int(contrast_correction * (self.blue - 128) + 128)
        return Color(new_red, new_green, new_blue)

    def __rmul__(self, other):
        return self.__mul__(other)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
       [bg_color] * 19,
       [bg_color] * 9 + [color] + [bg_color] * 9,
       [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
       [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
       [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
       [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
       [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
       [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
       [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':

    red = Color(255, 0, 0)
    print(red)

    green = Color(0, 255, 0)
    print(green)

    red2 = Color(255, 0, 0)
    print(red2)

    print(red + green)

    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(color_list)
    print(set(color_list))

    print(0.5 * red)

    print_a(green)
