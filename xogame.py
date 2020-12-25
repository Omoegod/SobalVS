import sys, os
import re

winner = "False"
coordinates = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
board = ["-","-","-","-","-","-","-","-","-"]
os.system('cls')

player = input('Выберете за кого будете играть Х или О: ')
if player == 'X':
    print('Вы играете за X')
else:
    print('Вы играете за О')


while winner == "False":
    print("   1   2   3 ")
    print("A  " + board[0] + " | " + board[1] + " | " + board[2])
    print("   ----------")
    print("B  " + board[3] + " | " + board[4] + " | " + board[5])
    print("   ----------")
    print("C  " + board[6] + " | " + board[7] + " | " + board[8])
    print("")
    if player:
        move = input("Игрок " + player + " выбери поле(Формат: A1-С3):")
        move = move.capitalize()
        choice = move
    else:
        move = input("Игрок " + player + " выбери поле(Формат: A1-С3):")
        move = move.capitalize()
        choice = move
    if not re.search('[ABC]+[123]', choice):
        input("Неправильный ввод, попробуйте снова..")
        continue
    else:
        place_coordinates = coordinates.index(choice)
        choicevaule = (board[place_coordinates])

        if choicevaule == "-":
                board[place_coordinates] = player
        else:
                print ("Эта позиция уже занята, выберете другую")
                input("Нажмите Enter, чтобы выбрать другую позицию...")
                continue

        if board[0] == player and board[1] == player and board[2] == player:
                winner = "True"
        if board[3] == player and board[4] == player and board[5] == player:
                winner = "True"
        if board[6] == player and board[7] == player and board[8] == player:
                winner = "True"
        if board[0] == player and board[3] == player and board[6] == player:
                winner = "True"
        if board[1] == player and board[4] == player and board[7] == player:
                winner = "True"
        if board[2] == player and board[5] == player and board[8] == player:
                winner = "True"
        if board[0] == player and board[4] == player and board[8] == player:
                winner = "True"
        if board[2] == player and board[4] == player and board[6] == player:
                winner = "True"
        if not "-" in board:
                stale = "yes"
                winner = "True"
        else:
                stale = "not"
                if player == "O":
                        player="X"
                else:
                        player="O"
        
        os.system('cls')

if player == "O":
        player="X"
else:
        player="O"

print("   1   2   3 ")
print("A  " + board[0] + " | " + board[1] + " | " + board[2])
print("   ----------")
print("B  " + board[3] + " | " + board[4] + " | " + board[5])
print("   ----------")
print("C  " + board[6] + " | " + board[7] + " | " + board[8])
print("")
if not stale == "yes":
    print("Игрок  " + player + "  Победил")
else:
    print("Ничья!")

 