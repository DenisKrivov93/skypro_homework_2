def card_mask(number: int) -> int:
    """Функция принимает номер карты числом и возвращает её с маской"""
    new_num = str(number)
    return new_num[:4] + ' ' + new_num[4:6] + '** **** ' + new_num[-4:]
