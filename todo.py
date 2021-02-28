import time

HELP = """
help     - список команд
add      - добавить задачу
remove   - удалить задачу
showall  - показать задачи
show     - показать задачи по дате
exit     - закрыть программу
"""

def checkTime(Date):
  try:
    time.strptime(Date, '%m.%d.%Y')
    return True
  except ValueError:
    print('Invalid date!')
    return False

def addTask(Date, Task):
  if Date in todo:
    todo[Date].append(Task)
  else:
    todo[Date] = [Task]
  print(f"задача {Task} добавлена\n" )

todo = {
  "12.12.2021":["Do 1", "Do 2"],
  "12.02.2021":["Do 3"]
}
userAnswer = ""
print("Для вывода списка команд введите help")

while True:
  userAnswer = input().lower()

  if userAnswer == "help":
    print( HELP )
  elif userAnswer == "add":
    uDate = input("Введите дату в формате mm.dd.yyyy\n")
    if checkTime(uDate) == False:
      continue

    uTask = input("Введите задачу\n")
    addTask(uDate, uTask)

  elif userAnswer == "remove":
    print( "задача удалена\n" )
  elif userAnswer == "showall":
    for i in sorted(todo.keys() ):
      for j in todo[i]:
        print( f"[{i}]\t {j} " )
  
  elif userAnswer == "show":
    uDate = input("Какую дату вы хотите посмотреть?\n")
    for i in sorted(todo.keys() ):
      if i==uDate:
        for j in todo[i]:
          print( f"[{i}]\t {j} " )

  elif userAnswer == "exit":
    print( "До свидания!\n" )
    break
  else:
    print("Вы ввели неизвестную команду")
    print("Для вывода списка команд введите help")
    