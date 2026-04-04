def messenger(name, chat):
    while True:
        with open(chat, 'a+', encoding='utf-8') as story_chat:
            try:

                do_choice = int(input(f'{name} , отправить сообщение - 1 просмотреть историю - 0: '))

                if do_choice == 1:
                    send_text = input('Введите сообщение: ')
                    story_chat.write(f'{name}.\n    {send_text}\n')

                elif do_choice == 0:
                    print('ИСТОРИЯ СООБЩЕНИЙ' + '\n')
                    story_chat.seek(0)
                    for i_string in story_chat:
                        print(i_string.rstrip())
                else:
                    raise ValueError('Укажите число 1 или 0. Отправить сообщение - 1 просмотреть историю - 0')
            except ValueError as exc:
                print(exc)


choice_the_name = input('Введите своё имя: ').title()
messenger(choice_the_name, 'chat.txt')
# Имитация происходит, путём вызова сторонней программы через терминал.
