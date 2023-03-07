VOWELS = ['a', 'e', 'i', 'o', 'u']

letter = input("Введите букву: ")

if letter in VOWELS:
    print(f"Буква '{letter}' главная")
elif letter == 'y':
    print(f"Буква '{letter}' может быть как гласной так и согласной")
else:
    print(f"Буква '{letter}' согласная")
