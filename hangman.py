import random


def hangman(word):  # Функция с игрой, параметр - слово, которое нужно отгадать
    words = ['idiot', 'retard', 'motherfucker', 'asshole', 'bastard']
    random_word = random.randint(0, 4)
    word = words[random_word]
    wrong = 0  # Кол-во ошибок в отгадывании букв
    stages = ['',  # Список с рисунком человека
              '________        ',
              '|               ',
              '|         |     ',
              '|         0     ',
              '|        /|\    ',
              '|         |     ',
              '|        / \    ',
              '|               '
              ]
    rletters = list(word)  # Переменная со списком неотгаданных букв
    board = ['__'] * len(word)  # Переменная, отвечающая за подсказки (отгаданные буквы) и выводящая _
    win = False  # Чтобы сразу не победил
    print('Welcome to the execution!')  # Начало игры
    while wrong < len(stages) - 1:  # Игра продолжается пока кол-во неправильных букв меньше кол-ва строк в рисунке
        print('\n')  # Сразу выводим пустую область для украшения
        msg = 'Input a letter: '  # Принимаем догадку игрока
        guess = input(msg)  # Сохраняем догадку в переменной
        if guess in rletters:  # Если догадка есть в списке неотгаданных букв
            cind = rletters.index(guess)  # Назначаем переменной индекс отгаданной буквы в самом слове
            board[cind] = guess  # Вставляем отгаданную букву в список слова
            rletters[cind] = '$'  # Если в слове 2 одинаковых буквы, первую заменяем на $
        else:  # Догадка была неправильной
            wrong += 1  # Увеличиваем значение на 1
        print((' '.join(board)))  # Выводим строчку с рез-том угадывания
        e = wrong + 1  # Назначаем переменную индекса с кол-вом ошибок + 1
        print('\n'.join(stages[0: e]))  # Делаем срез строки с человечком от 0 до wrong + 1
        if '__' not in board:  # Если мы отгадали все буквы
            print('You won! The word was: ')
            print(''.join(board))  # Выводим слово
            win = True  # Прерываем цикл
            break
    if not win:  # Если проиграл
        print('\n'.join(stages[0: wrong]))  # Выводится рисунок полностью
        print('You lost! The word was: '
              '{}.'.format(word))  # Вывод строки с указанием слова, которое игрок не смог угадать


hangman('execution')