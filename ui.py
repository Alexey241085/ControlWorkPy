import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите НАЗВАНИЕ заметки: '), number)
    body = check_len_text_input(
        input('Введите ТЕКСТ заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\n 'Заметки'. Выберете пункт меню:\n\n"
          "1 - Показать все заментки\n"
          "2 - Добавить заметку\n"
          "3 - Удалить заметку\n"
          "4 - Изменить заметку\n"
          "5 - Выбрать заметоку по дате\n"
          "6 - Показать заметку по id\n"
          "7 - Выход\n\n"
          "Выберете пункт меню: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть не менее {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("***** Ты заходи, если что *****")