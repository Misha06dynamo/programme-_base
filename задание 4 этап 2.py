print("Добро пожаловать в 'Менеджер заметок'!")
spisok_zam = []
while True:
    z1 = input("Введите имя пользователя: ")
    z2 = input("Введите заголовок заметки: ")
    z3 = input("Введите описание заметки: ")
    z4 = input("Введите статус заметки (новая, в процессе, выполнено): ")
    z5 = input("Введите дату создания (день-месяц-год): ")
    z6 = input("Введите дедлайн (день-месяц-год): ")

    note = (z1,z2,z3,z4,z5,z6)
    spisok_zam.append(note)
    add_smt = input("Хотите добавить ещё одну заметку? (да/нет): ")
    if add_smt == 'да':
        continue
    else:
        break

print("Ваши заметки:")
for note in spisok_zam:
    print(note)
