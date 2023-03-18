def is_strong_password(password: str) -> bool:
    is_strong_pass = False

    if len(password) < 8:
        return is_strong_pass

    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for symbol in password:
        if symbol.isupper():
            has_uppercase = True
        elif symbol.islower():
            has_lowercase = True
        elif symbol.isdigit():
            has_digit = True

        if has_uppercase and has_lowercase and has_digit:
            is_strong_pass = True
            return is_strong_pass

    return is_strong_pass


def main():
    description = """
    - Пароль должен состоять минимум из 8 символов;
    - должна быть хотя бы 1 буква в верхнем регистре;
    - должна быть хотя бы 1 буква в нижнем регистре;
    - должна быть хотя бы 1 цифра.
    """
    print(description)

    password = input("Введите пароль: ")

    if is_strong_password(password):
        print("Ваш пароль является надёжным")
    else:
        print("Ваш пароль не является надёжным")


if __name__ == '__main__':
    main()
