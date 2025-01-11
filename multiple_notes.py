from datetime import *

def create_note(): # функция создания заметки

    while True:#имя пользователя
        username = input("Введите имя пользователя: ")
        if not username:
            print("Имя пользователя не может быть пустым.")
            continue
        break

    while True:#заголовок заметки
        title = input("Введите заголовок заметки: ")
        if not title:
            print("Заголовок не может быть пустым.")
            continue
        break

    while True: #описание заметки
        content = input("Введите описание заметки: ")
        if not content:
            print("Описание не может быть пустым.")
            continue
        break

    while True: #статус заметки
        status = input("Введите статус заметки: ")
        if not status:
            print("Статус не может быть пустым.")
            continue
        break

    while True: # Дата создания заметки
        try:
            created_date_str = input("Введите дату создания заметки в формате дд-мм-гггг: ")
            created_date_obj = datetime.strptime(created_date_str, "%d-%m-%Y")
            break
        except:
            print("Неверный формат даты. Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024")

    while True:  # Дедлайн
        try:
            issue_date_str = input("Введите дату дедлайна в формате дд-мм-гггг: ")
            issue_date_obj = datetime.strptime(issue_date_str, "%d-%m-%Y")
            break
        except:
            print("Неверный формат даты. Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024")

    note = {  # список со всей информацией
        'Имя пользователя:': username,  # Имя пользователя
        'Заголовок:': title, # заголовок заметки
        'Описание заметки:': content,  # Описание заметки
        'Статус заметки:': status,  # Статус заметки
        'Дата создания заметки:': created_date_str,  # Дата создания заметки в формате дд-мм
        'Дата истечения заметки:': issue_date_str,  # Дата истечения заметки в формате дд-мм
    }
    return note


def title_unique(title, notes_list): #функция проверки уникальности заголовков
    for note in notes_list:
        if note['Заголовок:'] == title:
            return False
    return True


notes_list=[] #список для заметок
new_note="да"
print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')

while new_note=="да": # цикл добавления заметок
    while True: #проверка уникальности заголовка
        created_note=create_note()
        if title_unique(created_note['Заголовок:'], notes_list):
            notes_list.append(created_note)
            break
        else:
            print("Заметка с таким заголовком уже существует. Пожалуйста, введите другой заголовок.")

    new_note=input("Хотите добавить ещё одну заметку? (да/нет): ")
    if new_note=="нет":
        break

print("Список заметок:") #вывод списка заметок
number_=1
for i, item in enumerate(notes_list, start=1): # цикл вывода списка с заметками
    print(f"{i}. Имя пользователя: {item['Имя пользователя:']}")
    print(f"   Заголовок: {item['Заголовок:']}")
    print(f"   Описание заметки: {item['Описание заметки:']}")
    print(f"   Статус заметки: {item['Статус заметки:']}")
    print(f"   Дата создания заметки: {item['Дата создания заметки:']}")
    print(f"   Дата истечения заметки: {item['Дата истечения заметки:']}")

