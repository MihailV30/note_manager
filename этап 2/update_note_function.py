from datetime import datetime

def validate_date(date_str): #Проверяет корректность формата даты.
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def update_note(notes_list): #Обновляет заметку, позволяя пользователю выбрать поле для обновления.
    if not notes_list:
        print("Список заметок пуст.")
        return notes_list

    print("Текущие заметки:")
    for i, note in enumerate(notes_list):
        print(f"{i+1}. {note}")

    while True: #выбор номера заметки для обновления
        try:
            note_index = int(input("Введите номер заметки для обновления: ")) - 1
            if 0 <= note_index < len(notes_list):
                break
            else:
                print("Неверный номер заметки.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    updatable_fields = ["username", "title", "content", "status", "issue_date"]
    while True: #цикл работает пока пользователь не введет кореектное имя поля для обновления
        field_to_update = input(f"Какие данные вы хотите обновить? ({', '.join(updatable_fields)}): ").lower()
        if field_to_update in [f.lower() for f in updatable_fields]:
            break
        else:
            print("Некорректное имя поля. Пожалуйста, попробуйте еще раз.")

    while True: #если пользователь решил обновить дату, то цикл будет работать пока функция проверки даты не вернет True
        new_value = input(f"Введите новое значение для {field_to_update}: ")
        if field_to_update == "issue_date" and not validate_date(new_value):
            print("Некорректный формат даты. Используйте формат ДД-ММ-ГГГГ.")
        else:
            notes_list[note_index][field_to_update] = new_value
            break

    print("\nЗаметка обновлена:")
    print(notes_list[note_index])
    return notes_list

# Пример использования
'''
note = {
    'username': 'Алексей',
    'title': 'Список покупок',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '27-11-2024',
    'issue_date': '30-11-2024'
}
'''
#updated_note = update_note(note) #вызов закоментирован для корректной работы меню при импорте файла с ней

