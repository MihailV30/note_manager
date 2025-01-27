def search_notes(notes_list, keyword=None, status=None):
    keywords = [] # списки для хранения ключевых слов и результатов поиска
    results = []

    if not notes_list: #остановка поиска если нет заметок
        return print("Список заметок пуст")

    print("Поиск заметки")
    print('-' * 30)

    key = input("Введите ключевое слово (оставьте пустым, если не нужно): ")

    if key != "": # если пользователь ввел ключевое слово ему будет предлагать добавить ключевые слова
        keywords.append(key.strip().lower()) # запись ключевых слов в список
        while True:
            key_question = input("Продолжить добавление ключевых слов? (да/нет): ").lower()
            if key_question not in ["да","нет"]:
                print("Неверный ввод!")
            else: break

        if key_question != "нет":
            while True:
                key = input("Введите ключевое слово (оставьте пустым, чтобы остановить ввод или если не нужно): ")
                if key == "":
                    break
                keywords.append(key.strip().lower()) # запись ключевых слов в список


    status = input("Введите статус (оставьте пустым, если не нужно): ").strip().lower()

    if (len(keywords) == 0) and (not status): # если параметры поиск не введены то поиск останавливается
        return print(('-' * 30) + "\nПоиск остановлен по причине отсутствия параметров поиска")
    else:
        print(('-' * 30) + "\nПоиск выполняется по следующим параметрам:\nключевые слова:", (", ".join(keywords)),
              "\nстатус:", status)

    for i, note in enumerate(notes_list):  # цикл перебора заметок
        result_check = True # флаг для проверки соответствия критериям поиска
        if keywords: # проверка по ключевым словам, если они есть
            keyword_check = all(j in note['title'].lower().strip() or j in note['content'].lower().strip() or j in note['username'].lower().strip() for j in keywords) # проверка наличия всех ключевых слов в полях заметки (title, content, username)
            result_check = result_check and keyword_check # обновление флага, если ключевые слова не найдены
        if status: # проверка по статусу, если он есть
            result_check = result_check and (note['status'].lower().strip() == status)

        if result_check: # добавление заметки в результаты, если все критерии выполнены
            results.append((i + 1, note))

    if results: # вывод результатов поиска
        print(('-' * 30) + "\nНайдены заметки:\n" + ('-' * 30))
        for num, note in results:
            print(f"\nЗаметка №{num}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}")
            print(('-' * 30) + "\n")
    else:
        print('-' * 30)
        print("Заметки, соответствующие запросу, не найдены.")

    return notes_list

notes_list = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]

#search_notes(notes_list) #вызов закоментирован для корректной работы меню при импорте файла с ней