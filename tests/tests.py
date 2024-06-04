from src.masks import account_mask, card_mask


def multimask_func(user_input: str) -> str:
    """Выявляет какие данные ей предоставили и возвращает данные на основе заготовленных функций с масками"""
    key_words_cards = ["Visa Classic", "Visa Gold", "Maestro", "MasterCard"]
    payment_info = user_input.split(" ")
    payment_number = payment_info[-1]
    payment_name = " ".join(payment_info[:-1])
    if payment_name == "Счет":
        payment_number = account_mask(payment_number)
    elif payment_name in key_words_cards:
        payment_number = card_mask(payment_number)
    else:
        return "Приложение не работает с выбранным банком или введена некорректая информация"
    return f"{payment_name} {payment_number}"


print(multimask_func("Maestro 1596837868705199"))
