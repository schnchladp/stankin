"""Валидация номеров телефонов"""


import re

PhoneRe= r'(\+79)[0-9]{9}'

def is_valid_phone(num: str)-> bool:
    """
    Проверяет строку на синтаксическую корректность

    args:
        num: строка для проверки
    returns:
        true, если num корректен, false иначе
    examples:
        >>> is_valid_phone("+79000000000")
        True
        >>> is_valid_phone("79000000000")
        False
    """

    if type(num) != str:
        return False
    if not num or len(num)!=12:
        return False
    return re.match(PhoneRe, num) is not None






