b = []
while True:
    a = input("Введите заголовок:")
    if a == "":
        break
    b.append(a)

print("Заголовки заметки:")
for a in b:
    print("-",a)
