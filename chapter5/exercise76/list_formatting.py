def format_list(lst: list) -> str:
    temp_list = lst
    temp_list.insert(-1, 'и')
    text = ''

    for item in temp_list:
        if item != 'и' and item != temp_list[-3] and item != temp_list[-1]:
            text += item + ', '
        else:
            text += item + ' '

    return text


def main():
    lst = input("Введите список (через пробел): ").split()
    print(f"Отформатированный список: {format_list(lst)}")


if __name__ == '__main__':
    main()
