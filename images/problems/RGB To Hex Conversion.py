'''
The hex_value function is incomplete.
Complete it so that passing in hex_value decimal values will result in a hexadecimal representation being returned.
Valid decimal values for hex_value are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
'''


# Функция rgb принимает три аргумента: r, g, b - значения красного, зеленого и синего цветов соответственно.
# Функция возвращает строку, представляющую цвет в формате hex.
def rgb(r, g, b):

    hex_value = '' # Создаем пустую строку для хранения значения цвета в формате hex

    for i in [r, g, b]: # Проходим по каждому значению цвета rgb
        # округляем значения меньше 0 и больше 255
        if i <= 0:
            hex_value += '00'
        elif i > 255:
            hex_value += 'FF'

        else:
            current_hex_value = str(hex(i)).upper()[2:] # Переводим значение в шестнадцатеричное и удаляем первые два символа ('0x')
            if len(current_hex_value) == 1: # Если длина шестнадцатеричного значения равна 1, добавляем '0' перед ним
                hex_value += '0'
            hex_value += current_hex_value
    return hex_value # Возвращаем строку цвета в формате hex