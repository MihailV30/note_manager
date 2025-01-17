'''Проверка и обновление статуса заметки

Функциональность:
Показывает текущий статус заметки.
Предлагает изменить статус на один из предложенных.
Обрабатывает некорректный ввод.'''


current_status = "в процессе" #текущий статус
print("Текущий стату заметки:",repr(current_status)) #вывод текущего статуса
print("Выберите новый статус заметки:","1. выполнено","2. в процессе","3. отложено",sep = '\n') #выбор вариантов выбора статуса
user_status = input()

while user_status not in ["1","выполнено","2","в процессе","3","отложено"]: #проверка коректности выбора статуса
    # в случае неправильного выбора пользователю предложит заново выбрать статус
    print("Выбран некорректный статус заметки, выберите другой")
    user_status = input()

if user_status in ["1","выполнено"]: #выбор первого статуса
    print("Ваш выбор:",repr(user_status))
    print('Статус заметки успешно обновлён на: "выполнено"')
    current_status = {"выполнено"}

elif user_status in ["2","в процессе"]: #выбор второго статуса
    print("Ваш выбор:",repr(user_status))
    print('Статус заметки успешно обновлён на: "в процессе"')
    current_status = {"в процессе"}

elif user_status in ["3","отложено"]: #выбор третьего статуса
    print("Ваш выбор:",repr(user_status))
    print('Статус заметки успешно обновлён на: "отложено"')
    current_status = {"отложено"}

print("Текущий стату заметки:",repr(*current_status))