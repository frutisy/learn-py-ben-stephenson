from random import randint


def generate_password() -> str:
    length_password = randint(7, 10)
    password = ''
    lower_bound = 33
    upper_bound = 126

    for k in range(length_password):
        random_number = randint(lower_bound, upper_bound)
        password += chr(random_number)

    return password


def main():
    for k in range(5):
        password = generate_password()
        print(f"Сгенерированный пароль: {password}")


if __name__ == '__main__':
    main()
