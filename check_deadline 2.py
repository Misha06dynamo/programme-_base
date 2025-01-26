from datetime import datetime
deadline=input("Введите дату дедлайна (формат: день-месяц-год): ")
deadline_date = datetime.strptime(deadline,"%d-%m-%Y")
current_date = datetime.now()
dead2 = (deadline_date - current_date).days
if dead2 > 0:
    print(f"До дедлайна осталось {dead2} {'день' if dead2 == 1 else 'дня' if dead2 < 5 else 'дней'}.")
elif dead2 == 0:
    print("Дедлайн сегодня!")
else:
    print(f"Внимание! Дедлайн истёк {-dead2} {'день' if -dead2 == 1 else 'дня' if -dead2 < 5 else 'дней'} назад.")
