import re

def validate_name(name: str) -> bool:
    regex = re.compile(r'[а-яА-Я]{1,15}')
    if regex.fullmatch(name):
        return True
    return False

def validate_phone_number(phone_nubmer: str) -> bool:
    regex = re.compile(r'[0-9]{1,15}')
    if regex.fullmatch(phone_nubmer):
        return True
    return False
