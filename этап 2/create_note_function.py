import datetime

def validate_date(date_str): # проверяет корректность формата даты

    try:
        day, month, year = map(int, date_str.split('-'))
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False

def create_note(notes_list): # Создает новую заметку и возвращает ее данные в виде словаря, проверяя коректность ввода

    username = input("Введите имя пользователя: ")
    while not username:
        print("Имя пользователя не может быть пустым!")
        username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    while not title:
        print("Заголовок не может быть пустым!")
        title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    while not content:
        print("Описание не может быть пустым!")
        content = input("Введите описание заметки: ")

    status_options = ["новая", "в процессе", "выполнено"]
    print("Выберите статус заметки:")
    for i, status_option in enumerate(status_options): #цикл перебором выводит в консоль доступные для выбора статусы
        print(f"{i + 1}. {status_option}")

    while True: #проверка коректности выбора статуса
        try:
            status_choice = int(input("Введите номер статуса: "))
            if 1 <= status_choice <= len(status_options): #Проверяет, находится ли введенный номер в допустимом диапазоне от 1 до количества элементов в списке
                status = status_options[status_choice - 1]
                break
            else:
                print("Неверный номер статуса.")
        except:
            print("Неверный ввод. Введите число.")

    print("Установлен статус:", status)

    while True: #цикл работает пока пользователь не введет правильное значение даты
        issue_date_str = input("Введите дату дедлайна (дд-мм-гггг, например, 30-11-2024): ")
        if validate_date(issue_date_str): #если функция проверки даты возвращает True, то дата присваивается переменной issue_date
            issue_date = issue_date_str
            break
        else:
            print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")

    current_date = datetime.date.today().strftime("%d-%m-%Y")

    note = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': current_date,
        'issue_date': issue_date
    }
    notes_list.append(note)

    note_summary = (
        "------------------------------\n"
        "Создана новая заметка:\n"
        f"  Пользователь: {note['username']}\n"
        f"  Заголовок: {note['title']}\n"
        f"  Описание: {note['content']}\n"
        f"  Статус: {note['status']}\n"
        f"  Дата создания: {note['created_date']}\n"
        f"  Дедлайн: {note['issue_date']}"
    )
    print("------------------------------")
    print("Заметка создана!")
    return notes_list

#notes_list=[]

#create_note(notes_list) #вызов закоментирован для корректной работы меню при импорте файла с ней
