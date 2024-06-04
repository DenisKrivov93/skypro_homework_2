from src.masks.account_mask import account_mask
from src.masks.card_mask import card_mask


def multimask_func(user_input: str) -> str:
    """Выявляет какие данные ей предоставили и возвращает данные на основе заготовленных функций с масками"""
    key_word_account = "Счет"
    key_word_visa_classic = "Visa Classic"
    key_word_visa_platinum = "Visa Platinum"
    key_word_visa_gold = "Visa Gold"
    key_word_maestro = "Maestro"
    key_word_mastercard = "MasterCard"
    if key_word_account in user_input:
        return "Счет " + account_mask(user_input[-4:])
    elif key_word_visa_classic in user_input:
        return "Visa Classic " + card_mask(user_input[-16:])
    elif key_word_visa_platinum in user_input:
        return "Visa Platinum " + card_mask(user_input[-16:])
    elif key_word_visa_gold in user_input:
        return "Visa Gold " + card_mask(user_input[-16:])
    elif key_word_maestro in user_input:
        return "Maestro " + card_mask(user_input[-16:])
    elif key_word_mastercard in user_input:
        return "MasterCard " + card_mask(user_input[-16:])
    else:
        return "Приложение не работает с выбранным банком или введена некорректая информация"




print(multimask_func("Maero 6831982476737658"))


