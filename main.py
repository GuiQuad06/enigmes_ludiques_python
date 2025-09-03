from nim import Nim

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    my_nim = Nim(n = 21, p = 3)
    player1_name = input('Please enter your name, player 1: ')
    player2_name = 'bot'
    players = (player1_name, player2_name)
    turn = 0

    while my_nim.cpt > 1:
        print(my_nim)
        if players[turn] == 'bot':
            print('Bot is playing...')
            my_nim.bot_play()
        else:
            print(f'Please proceed {players[turn]}')
            play = int(input('How many ?'))
            my_nim.play(play)
        turn = (turn + 1) % 2

    print(f'You lost {players[turn]}')