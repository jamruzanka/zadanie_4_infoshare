import random
from sys import exit

def start_game():
    print("Zagrajmy w klasyczną grę papier, nożyce kamień.")
    print("Wybierz swoje zagranie, wpisując odpowiednią literę: (P)apier, (N)ożyce, (K)amień")

def computer():
    choices = ['Papier','Nożyce','Kamień']
    computer_choice = random.choice(choices)
    print("Komputer:",computer_choice)
    return computer_choice

def player():
    user_input = input("Twoje zagranie: ")
    if user_input == 'p' or user_input == 'P':
        player_choice = 'Papier'
        print("Gracz: Papier")
        return player_choice
    elif user_input == 'n' or user_input == 'N':
        player_choice = 'Nożyce'
        print("Gracz: Nożyce")
        return player_choice
    elif user_input == 'k' or user_input == 'K':
        player_choice = 'Kamień'
        print("Gracz: Kamień")
        return player_choice
    else:
        print("Żeby wybrać zagranie, wpisz odpowiednią literę")
        user_input = input("Twoje zagranie: ")
        if user_input in ['p','P','n','N','k','K']:
            player_choice()
        else:
            print("Chyba nie potrafisz się zdecydować. Do następnego razu!")
            exit(0)

def duel():
    player_choice = player()
    computer_choice = computer()

    if player_choice == computer_choice:
        print("Mamy remis!")
        play_again()
    elif player_choice == 'Papier' and computer_choice == 'Kamień':
        print("Wygrałeś!")
        play_again()
    elif player_choice == 'Nożyce' and computer_choice == 'Papier':
        print("Wygrałeś!")
        play_again()
    elif player_choice == 'Kamień' and computer_choice == 'Nożyce':
        print("Wygrałeś!")
        play_again()
    else:
        print("Niestety, tym razem przegrałeś.")
        play_again()

def play_again():
    print("Chcesz zagrać jeszcze raz?")
    user_answer = input('[y/n]')
    if user_answer == 'Y' or user_answer == 'y':
        duel()
    elif user_answer == 'N' or user_answer == 'n':
        exit(0)
    else:
        print("Nie rozumiem co chcesz zrobić - wybierz [y], jeśli chcesz grać albo [n], jeśli masz już dość.")
        user_answer = input('[y/n]')
        if user_answer == 'Y' or user_answer == 'y':
            duel()
        elif user_answer == 'N' or user_answer == 'n':
            exit(0)
        else:
            print("Chyba się nie dogadamy - na dziś koniec!")
            exit(0)

start_game()
duel()
