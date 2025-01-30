from datetime import datetime

def note():
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    issue_date = input("Введите дату дедлайна (день-месяц-год): ")

    created_date = datetime.now().strftime("%d-%m-%Y")
    if created_date>issue_date:
        print("Время дедлайна истекло!")
    elif created_date==issue_date:
        print("Дедлайн сегодня!")
    else:
        print("Всё хорошо! Время ещё есть")
    note2 = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date
    }

    print("Заметка готова:", note2)
note()
