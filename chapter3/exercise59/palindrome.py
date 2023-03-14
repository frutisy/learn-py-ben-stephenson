text = input("Введите строку: ")

for i in range(len(text)):
    if text[i] != text[- 1 - i]:
        print("Введённая строка не является палиндромом")
        break
else:
    print(f"Строка '{text}' является палиндромом")
