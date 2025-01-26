status=input("Введите статус(выполнено, в процессе, отложено):")
status2=["выполнено","в процессе","отложено"]
print(status)
while True:
    new_status=input("Введите новый статус:")
    if new_status in status2:
        status=new_status
        break
    else:
        print("Ошибка! Введите корректно")
print(status)
