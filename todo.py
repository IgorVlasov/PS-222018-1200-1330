HELP = """
help      -
add       -
remove    - 
show      -
exit      -

"""


todo = {}
userAnswer = ""

while True:
  userAnswer = input()

  if userAnswer == "help":
    print(HELP)
  elif userAnswer == "add":
    print("Задача добалена")
  elif userAnswer == "remove":
    print("Задача удалена")
  elif userAnswer == "show":
    print("Задача показана")
  elif userAnswer == "exit":
    print("Завершение!")
    break
  else:
    print("Вы ввели неизвестную задачу")
    print("Для вывода списка команд введите help")
