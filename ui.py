import helpers


def display_board(board, hero):
    '''
    Displays complete game board on the screen
    

    Returns:
    Nothing
    '''

    for i in range(len(board)):
        if i in range(len(hero)):
            print(f"{str(hero[i]).ljust(15) + ''.join(board[i])}")
        else:
            print(f"{15*' ' + ''.join(board[i])}")
    
    # helpers.clear_screen()
    # for row in board:
    #     print(''.join(row))  # ???

def display_ascii(ascii_art):
    print(ascii_art)


def display_items(items):
    print('X' + 98*'~' + 'X')
    print(f"|{98*' '}|")
    for key in items:
        print(f"| \t{(key + ': ').ljust(90)} |")
        for element in items[key]:
            print(f"|\t\t{element.ljust(83)}|")
        print(f"|{98*' '}|")
    print(f"|{98*' '}|")
    print('| ' + "\tPress 'Q' to quit.".ljust(90) + '  |')
    print(f"|{98*' '}|")
    print('X' + 98*'~' + 'X')


def display_dialog_window(text):
    print('X' + 118*'~' + 'X')
    print(f"|{118*' '}|")
    text = text.split("\n")
    for line in text:
        print(f"|{line.center(118)}|")
    # else:
    #     print(f"|{text.center(118)}|")

    print(f"|{118*' '}|")
    print('X' + 118*'~' + 'X')


def about_authors():
    helpers.clear_screen()
    print("--- About Authors ---".center(100))
    print("\n\tStanisław Chynek (ES) - Senior Ascii Developer and Advanced Spitfire Pilot\n\tTomasz Makowski (Rlyyah) - Champion of Jaworzno City in Bubble Soccer\n\tAnna Mazurek (Bearded Lady) - Senior Scratch Developer, worked with the best Game Developers in Poland.\n\n")
