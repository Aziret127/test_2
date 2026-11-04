# """ОПЕРАТОРЫ ПРЕДНАДЛЕЖНОСТИ in """
# WORD = "Python"
# print("P" in WORD)  


# days_in_month = range(1, 31)
# days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# day = int(input("Введите количество дней: "))
# month = int(input("Введите номер месяца: "))

# if month not in days_in_month:
#     print("Такого месяца не существует")

# elif (month == 3 and day in range(1, 21)) or (month == 4 and day in range(21, 31)):
#      sing = "Овен"
# elif (month == 4 and day in range(21, 31)) or (month == 5 and day in range(1, 22)):
#     sing = "Телец"
# elif (month == 5 and day in range(22, 32)) or (month == 6 and day in range(1, 22)):
#     sing = "Близнецы"

# elif (month == 6 and day in range(22, 31)) or (month == 7 and day in range(1, 23)):
#     sing = "Рак"

# elif (month == 7 and day in range(23, 32)) or (month == 8 and  day in range(1, 24)):
#     sing = "Лев"

# elif (month == 8 and day in range(24, 32)) or (month == 9 and day in range(1, 24)):
#     sing = "Дева"

# elif (month == 9 and day in range(24, 32)) or (month == 10 and day in range(1, 24)):
#     sing = "Весы"

# elif (month == 10 and day in range(24, 32)) or (month == 11 and day in range(1, 23)):
#     sing = "Скорпион"

# elif (month == 11 and day in range(23, 32)) or (month == 12 and day in range(1, 22)):
#     sing = "Сстрелец"

# elif (month == 12 and day in range(22, 32)) or (month == 1 and day in range(1, 21)):
#     sing = "Козерог"

# elif (month == 1 and day in range(21, 32)) or (month == 2 and day in range(1, 20)):
#     sing = "Водолей"

# elif (month == 2 and day in range(20, 32)) or (month == 3 and day in range(1, 21)):
#     sing = "Рыбы"

#     print("Ваш знак:", sing)
# else :
    
#     print("Такого дня не существует")

"""цикл while"""

# counter = 0 
# while counter < 100:
#     counter += 1
#     if counter  == 50:
#         break
#     if counter % 2 == 0:
        
#         continue
#     print(counter)

n = 5

# while n > 0:
#      print(n)
#      n -= 1   
    
# print("Выход из цикла")


age_counter = 0
student_counter = 0

while True:
    age = input("Введите возраст студента: ")
    if age.isnumeric():
        age_counter += int(age)
        student_counter += 1
    else:
        print("вы ввели не число")
        break
    # print(student_counter)
print(f"Средний возраст студентов:"
      f" {round(age_counter / student_counter, 2)}"
)