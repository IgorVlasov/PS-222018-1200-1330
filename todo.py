import time

HELP = """
help      - показывает список команд
add       - добавить
remove    - удалить
showall   - показать все задачи
show      - показать задачи по указанной дате
exit      - выход
"""

def checkTime(Date):
  try:
    time.strptime(Date, '%m.%d.%Y')
    return True
  except ValueError:
    print('Неверно введена дата!')
    return False

def addTask(Date, Task):
  if Date in todo:
      todo[Date].append(Task)
  else:
      todo[Date] = [Task]
  print(f"Задача {Task} добалена\n")

todo = {
  "12.12.2021":["Тестовая задача 1", "Тестовая задача 2"],
  "11.11.2021":["Тестовая задача 3"],
}
userAnswer = ""

while True:
  userAnswer = input().lower()

  if userAnswer == "help":
    print(HELP)


  elif userAnswer == "add":
    uDate = input("Введите дату выполнения в формате mm.dd.yyyy\n")
    if checkTime(uDate) == False:
      continue
    uTask = input("Введите задачу\n")
    addTask(uDate, uTask)


  elif userAnswer == "remove":
    print("Задача удалена\n")


  elif userAnswer == "showall":
    for i in sorted(todo.keys()):
      for j in todo[i]:
        print(f"[{i}]\t {j}")


  elif userAnswer == "show":
    uInput = input("Введите дату выполнения в формате mm.dd.yyyy\n")
    if uInput in todo.keys():
      for i in todo[uInput]:
        print(f"[{uInput}]\t {i}")
    elif checkTime(uInput) == True:
      print("Нет задач по указанной дате")


  elif userAnswer == "exit":
    print("Завершение!\n")
    break

    
  else:
    print("Вы ввели неизвестную задачу")
    print("Для вывода списка команд введите help")
