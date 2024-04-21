import re

def is_empty(field):
    result = True
    if not field.strip():
        result = False
    return result

def is_valid_characters_count(field, number):
    result = False
    if len(field.strip()) > number:
        result = True
    return result

def is_digit(field):
    result = False
    reg = r"^\d+$"  #regex para dígitos
    if re.match(reg, field):
        result = True
    return result

def is_valid_digit(field):
    result = False
    reg = r"^(0|[1-9]\d*)$"  #regex para dígitos enteros positivos > 0
    if re.match(reg, field):
        result = True
    return result

def is_valid_decimal(field):
    result = False
    reg = r"^(0*[1-9][0-9]*(\.[0-9]+)?|0+\.[0-9]*[1-9][0-9]*)$"  #regex para dígitos decimales positivos > 0
    if re.match(reg, field):
        result = True
    return result

def is_valid_alpha(field):
    result = False
    reg = r"^[A-Za-zÑñÁáÉéÍíÓóÚú\s]+$"
    if re.match(reg, field):
        result = True
    return result

def is_valid_email(field):
    result = False
    reg = r"^[A-Za-z0-9]+[.-_]*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$"
    if re.match(reg, field):
        result = True
    return result

def is_valid_phone(field):
    result = False
    reg = r"^\(?\+?(\d{2}|\d{3})\)?\s?((\d{6}|\d{8})|(\d{3}[\*\.\-\s]){3}|(\d{2}[\*\.\-\s]){4}|(\d{4}[\*\.\-\s]){2})|\d{8}|\d{10}|\d{12}$"
    if re.match(reg, field):
        result = True
    return result

def is_valid_address(field):
    result = False
    reg = r"^[A-Za-zÑñÁáÉéÍíÓóÚú\s0-9,./#]+$"
    if re.match(reg, field):
        result = True
    return result

def is_valid_id(id):
    result = False
    reg = r"^\d{11}$"
    if re.match(reg, id):
        year = int(id[:2])
        month = int(id[2:4])
        day = int(id[4:6])
        if 0 < month <= 12 and day > 0:
            if month == 2 and day <= 28:
                result = True
            elif month == 2 and (year % 4 == 0) and day <= 29:
                result = True
            elif (month == 4 or month == 6 or month == 9 or month == 11) and day <= 30:
                result = True
            elif month != 2 and day <= 31:
                result = True
    return result

def is_valid_age(id):
    result = False
    if  get_age_by_id(id) >= 18:
        result = True
    return result

def is_valid_account(num):
    result = False
    reg = r"^\d{16}$"
    if re.match(reg, num):
        result = True
    return result

def get_age_by_id(id):
    now = datetime.now()
    if id[0] in ("0", "1", "2"):
        year_now = now.year - 2000
    else:
        year_now = now.year - 1900
    month_now = now.month
    day_now = now.day
    year_id = int(id[0:2])
    month_id = int(id[2:4])
    day_id = int(id[4:6])

    age = year_now - year_id
    if month_now < month_id or (month_now == month_id and day_id > day_now):
        age -= 1
    return age
