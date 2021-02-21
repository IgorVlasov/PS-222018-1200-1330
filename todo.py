import time

HELP = """
help    - список команд
add     - добавить задачу
remove  - удалить задачу
show    - показать задачи
exit    - показать задачи
"""

todo = {}
userAnswer = ""

print("Для вывода доступных команд отправте help")
while True:
    userAnswer = input().lower()

    if userAnswer == "help":
        print( HELP )
    elif userAnswer == "add":
        print("Введите дату в формате мм.дд.гг")
        uDate = input()
        try:
            valid_date = time.strptime(uDate, "%m.%d.%y")
        except ValueError:
            print('Неверный формат даты')
            continue
        print("\nВведите задачу")
        uTask = input()
        if uDate in todo:
            todo[uDate].append(uTask)
        else:
            todo[uDate]= [uTask]
        print(f"\nЗадача {uTask} добавлена")
        print("\n\n")
    elif userAnswer == "remove":
        print("Задача удалена")
        print("\n\n")
    elif userAnswer == "show":
        print("Задачи: ")
        for i in todo.keys():
            for j in todo[i]:
                print (f"[{i}]\t {j}")
        print("\n")
    elif userAnswer == "exit":
        print("Вы вышли из todo листа\n")
        break
    else:
        print("Вы ввели неизвестную команду")
        print("Для вывода доступных команд отправте help")
    