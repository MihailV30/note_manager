'''Удаление заметок

Функциональность:
Удаляет заметку по имени пользователя или заголовку.
Выводит сообщение, если заметка не найдена.
Обновляет список заметок.'''

def delete_note(notes_list):

    start_len = len(notes_list)

    if not notes_list:    #вывод списка заметок
        print("Список заметок пуст.")
        return notes_list
    else:
        print("Текущие заметки:")
        number_ = 1
        for i, item in enumerate(notes_list, start=1):#цикл вывода списка с заметками
            print(f"{i}. Имя: {item['username']}")
            print(f"   Заголовок: {item['title']}")
            print(f"   Описание: {item['content']}")
            print("")

    delete_criteria = input("Введите имя пользователя или заголовок для удаления заметки: ").lower()
    index = 0
    while index < len(notes_list): #цикл перебирающий список в поисках нужного критерия
        if delete_criteria in notes_list[index]['username'].lower() or delete_criteria in notes_list[index]['title'].lower():
            print("Заметка с выбранным критерием существует:",'\n',notes_list[index])
            if input("Вы уверены, что хотите удалить заметку? (да/нет) ")=="да":
                del notes_list[index] #если нужный критерий найден словарь удаляется из списка
                print("Заметка удалена!")
            else:
                index += 1  # иначе проверяется следующий элемент
        else:
            index += 1 #иначе проверяется следующий элемент

    if len(notes_list) < start_len: #если длина списка уменьшилась значит произошло удаление
        print("Успешно удалено. Остались следующие заметки:")
        if not notes_list: #если список пуст все заметки удалены
            print("Список заметок пуст.")
        else: # иначе выводятся имеющиеся заметки
            for i, item in enumerate(notes_list, start=1):
                print(f"{i}. Имя: {item['username']}")
                print(f"   Заголовок: {item['title']}")
                print(f"   Описание: {item['content']}")
                print("")
    else: #если длина списка не изменилась значит необходый критерий не найден
        print("Заметок с таким именем пользователя или заголовком не найдено.")

    return notes_list

'''
notes_list = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]
'''
#delete_note(notes_list) #вызов закоментирован для корректной работы меню при импорте файла с ней