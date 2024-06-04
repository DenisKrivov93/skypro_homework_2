def account_mask(number: int) -> int:
    """Функция принимает номер счета числом и возвращает его с маской"""
    new_num = str(number)
    return '**' + new_num[-4:]

