from colorama import Fore, Style, init

init()

translation = { # словарь для перевода ключей для последующего вывода
    'username': 'Имя пользователя',
    'title': 'Заголовок',
    'content': 'Описание',
    'status': 'Статус',
    'created_date': 'Дата создания',
    'issue_date': 'Дедлайн'
}

def display_notes(notes_list, detail_level="full"):
    if not notes_list: # проверка пустой заметки
        print(Fore.YELLOW + "У вас нет сохранённых заметок." + Style.RESET_ALL)
        return notes_list

    print(Fore.GREEN + "Что необходимо вывести:\n" + Style.RESET_ALL +
          "1. " + Fore.CYAN + "заголовки\n" + Style.RESET_ALL +
          "2. " + Fore.CYAN + "полную информацию\n" + Style.RESET_ALL +
          "(выберите номер, или оставть поле пустым для выхода)")

    while True: # цикл для выбора уровня детализации вывода
        choice = input(Fore.GREEN + "Ваш выбор: " + Style.RESET_ALL)
        print()
        if choice == '1':
            detail_level = "title"
            break
        elif choice == '2':
            detail_level = "full"
            break
        elif choice == '':
            print(Fore.YELLOW + "Операция отменена." + Style.RESET_ALL)
            return notes_list
        else:
            print(Fore.RED + "Неверный ввод. Попробуйте ещё раз." + Style.RESET_ALL)

    if notes_list: # проверка на пустой список после отмены операции
        print(Fore.GREEN + "Список заметок:" + Style.RESET_ALL)
        print('-' * 30)

        for i, note in enumerate(notes_list):
            print(Fore.CYAN + f"Заметка №{i + 1}:" + Style.RESET_ALL)
            if detail_level == "full":
                for key, value in note.items():
                    print(f"{translation.get(key, key)}: {value}")
            elif detail_level == "title":
                print(f"{translation['title']}: {note['title']}")
            print('-' * 30)
    return notes_list
'''
notes_list = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'}
]'''

#display_notes(notes_list) # вызов закоментирован для корректной работы меню при импорте файла с ней