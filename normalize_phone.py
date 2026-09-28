import re
def normalize_phone(phone_number):
    digits = re.sub(r'\D', '', phone_number)
    if len(digits) == 10:
        return f'(+38{digits[:10]})'
    elif len(digits) == 12 and digits.startswith('38'):
        return f'(+{digits[:12]})'
    else:
        return 'Invalid phone number'
    