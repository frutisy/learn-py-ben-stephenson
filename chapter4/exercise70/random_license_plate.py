from random import randint


def generate_rand_license_plate() -> str:
    letters = 'АВЕКМНОРСТУХ'
    digits = '0123456789'
    license_plate = ''

    is_new_license_plate = randint(0, 1)

    if is_new_license_plate:
        size = 4
        for i in range(size):
            rand_digit = randint(0, len(digits) - 1)
            license_plate += digits[rand_digit]

        size = 3
        for i in range(size):
            rand_letter = randint(0, len(letters) - 1)
            license_plate += letters[rand_letter]
    else:
        size = 3
        for i in range(3):
            rand_letter = randint(0, len(letters) - 1)
            license_plate += letters[rand_letter]

        for i in range(3):
            rand_digit = randint(0, len(digits) - 1)
            license_plate += digits[rand_digit]

    return license_plate


for k in range(10):
    print(f"{k + 1} - случайный номерной знак - {generate_rand_license_plate()}")
