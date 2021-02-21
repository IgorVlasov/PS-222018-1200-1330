import time

HELP = """
help   - показывает список команд
add    - добавить
remove - удалить
show   - показать
exit   - выход
"""


todo = {}
userAnswer = ""

while True:
  userAnswer = input().lower()

  if userAnswer == "help":
    print(HELP)
  elif userAnswer == "add":
    print("Введите дату выполнения в формате mm.dd.yyyy")
    uDate = input()
    try:
      valid_date = time.strptime(uDate, '%m.%d.%Y')
    except ValueError:
      print('Неверно введена дата!')
      continue
      
    print("Введите задачу")
    uTask = input()
    if uDate in todo:
      todo[uDate].append(uTask)
    else:
      todo[uDate] = [uTask]
    print(f"Задача {uTask} добалена\n")
  elif userAnswer == "remove":
    print("Задача удалена\n")
  elif userAnswer == "show":
    for i in sorted( todo.keys() )  
      for i in todo.keys():
        print(f"[{i}]\t {todo[i]} ")
  elif userAnswer == "exit":
    print("Завершение!\n")
    break
  else:
    print("Вы ввели неизвестную задачу")
    print("Для вывода списка команд введите help")
