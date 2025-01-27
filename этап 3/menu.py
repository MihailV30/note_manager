import colorama
from colorama import Fore, Style, init

init()

import create_note_function
import display_notes_function
import update_note_function
import delete_note
import search_notes_function

def menu():
    actions = {
        '1': create_note_function.create_note,
        '2': display_notes_function.display_notes,
        '3': update_note_function.update_note,
        '4': delete_note.delete_note,
        '5': search_notes_function.search_notes,
        '6': exit
        }

    notes_list = []

    while True:
        print()
        print(Fore.GREEN + "Доступные действия:" + Style.RESET_ALL)
        print(Style.BRIGHT + ('-' * 30) + Style.RESET_ALL)
        print(Fore.CYAN + "1: Создать новую заметку.\n2: Показать все заметки.\n3: Обновить заметку.\n4: Удалить заметку.\n5: Найти заметки." + Style.RESET_ALL)
        print(Fore.YELLOW + "6: Выйти из программы." + Style.RESET_ALL)
        print(Style.BRIGHT + ('-' * 30) + Style.RESET_ALL)

        user_choice = input(Fore.GREEN + "Введите номер действия: " + Style.RESET_ALL)
        print()
        print(Fore.CYAN + "Ваш выбор:" + Style.RESET_ALL, Fore.GREEN + user_choice + Style.RESET_ALL)
        print(Style.BRIGHT + ('-' * 30) + Style.RESET_ALL)

        try:
            if user_choice == '6':
                print(Fore.GREEN + "Программа завершена. Спасибо за использование!" + Style.RESET_ALL)
                break  # Выход из цикла
            elif user_choice not in actions:
                raise ValueError
            elif user_choice == '1':
                notes_list = create_note_function.create_note(notes_list)
                continue
            elif user_choice == '2':
                notes_list = display_notes_function.display_notes(notes_list)
                continue
            else:
                notes_list = actions[user_choice](notes_list)
                continue
        except ValueError:
            print(Fore.RED + "Неверный выбор. Пожалуйста, выберите действие из списка." + Style.RESET_ALL) # обработка неверного выбора
            print("\n")
            continue
        except Exception as e:
            print(Fore.RED + f"Произошла непредвиденная ошибка: {e}" + Style.RESET_ALL) # Обработка других ошибок

notes_list = menu()