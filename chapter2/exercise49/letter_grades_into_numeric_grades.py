LETTER_GRADES = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0
}

letterGrade = input("Введите буквенную оценку (например, 'A+'): ")

if letterGrade not in LETTER_GRADES.keys():
    raise ValueError("Вы ввели небуквенную оценку")

print(f"{letterGrade} в числовом виде {LETTER_GRADES[letterGrade]}")
