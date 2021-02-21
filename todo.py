import time

HELP = """
help    - список команд
add     - добавит задачу
remove  - удалить задачу
show    - показать задачи
exit    - закрыть программу
"""

todo = {}
userAnswer = ""
print("Для вывода списка команд введите help")

while True:
  userAnswer = input().lower()

  if userAnswer == "help":
    print( HELP )
  elif userAnswer == "add":
    print("Введите дату в формате mm.dd.yyyy")
    uDate = input()
    try:
      valid_date = time.strptime(uDate, '%m.%d.%Y')
    except ValueError:
      print('Invalid date!')
      continue

    print("Введите задачу")
    uTask = input()
    if uDate in todo:
      todo[uDate].append(uTask)
    else:
      todo[uDate] = [uTask]
    print ( f"задача {uTask} добавлена\n" )
  elif userAnswer == "remove":
    print ( "задача удалена\n" )
  elif userAnswer == "show":
    for i in sorted( todo.keys() ):
      for j in todo[i]:
        print ( f"[{i}]\t {j} " )
  elif userAnswer == "exit":
    print ("Досвидания!\n" )
    break
  else:
    print("Вы ввели неизвестную команду")
    print("Для вывода списка команд введите help")

  
