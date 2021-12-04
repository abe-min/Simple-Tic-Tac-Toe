#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 01:06:27 2020

@author: abrehammindaye
"""

N = ' ' #NULL Palce holder 
gameStatus = bool(True)
userinpt = [N,N,N,N,N,N,N,N,N]
xwon = bool(False)
owon = bool(False)
index_coordinate_dict = {(1,1):0, (1,2):1, (1,3):2, (2,1):3, (2,2):4, (2,3):5,(3,1):6, (3,2):7, (3,3):8} #This relates an an x,y coordinaet system to the list usrinpt

def prompt():
    v, w = input('Enter the coordinates: ').split()
    global x
    global y
    x, y = map(int, (v,w))
    validate(v,w)


def check_win():
    global xwon
    global owon
    global gameStatus
    if ((userinpt[0] == 'X' and userinpt[1] == 'X' and userinpt[2] == 'X') or (userinpt[3] == 'X' and userinpt[4] == 'X' and userinpt[5] == 'X') or (userinpt[6] == 'X' and userinpt[7] == 'X' and userinpt[8] == 'X') or (userinpt[0] == 'X' and userinpt[3] == 'X' and userinpt[6] == 'X') or (userinpt[1] == 'X' and userinpt[4] == 'X' and userinpt[7] == 'X') or (userinpt[2] == 'X' and userinpt[5] == 'X' and userinpt[8] == 'X') or (userinpt[0] == 'X' and userinpt[4] == 'X' and userinpt[8] == 'X') or (userinpt[2] == 'X' and userinpt[4] == 'X' and userinpt[6] == 'X')):
        xwon = True
        gameStatus = False
        print('X wins')

    if ((userinpt[0] == 'O' and userinpt[1] == 'O' and userinpt[2] == 'O') or (userinpt[3] == 'O' and userinpt[4] == 'O' and userinpt[5] == 'O') or (userinpt[6] == 'O' and userinpt[7] == 'O' and userinpt[8] == 'O') or (userinpt[0] == 'O' and userinpt[3] == 'O' and userinpt[6] == 'O') or (userinpt[1] == 'O' and userinpt[4] == 'O' and userinpt[7] == 'O') or (userinpt[2] == 'O' and userinpt[5] == 'O' and userinpt[8] == 'O') or (userinpt[0] == 'O' and userinpt[4] == 'O' and userinpt[8] == 'O') or (userinpt[2] == 'O' and userinpt[4] == 'O' and userinpt[6] == 'O')):
        owon = True
        gameStatus = False
        print('O wins')
    if ' ' not in userinpt and (xwon == False and owon == False):
        print ('Draw')
        gameStatus = False

def validate (v,w):
    global x
    global y
    try:
        int(v)
        int(w)
        x, y = map(int, (v,w))

        if x > 3 or y > 3:
            print('Coordinates should be from 1 to 3!')
            prompt()

        elif userinpt[index_coordinate_dict[x,y]] == ' ':
            pass
        else:
            print('This cell is occupied! Choose another one!')
            prompt()
    except:
        print('Enter numbers only')
        prompt()



while gameStatus==True:

    PlayerSelect = int(input("Enter 1 for player 1 and 2 for Player 2: "))

    if PlayerSelect == 1:
        P = 'X'
    else:
        P = 'O'
    v, w = input('Enter the coordinates: ').split()

    validate(v,w)

    for elem in userinpt:
        userinpt[index_coordinate_dict[x,y]] = P

    def theBoard ():
        print('---------')
        print('|' + " " + userinpt[0] + " " + userinpt[1] + " " + userinpt[2] + " " + '|')
        print('|' + " " + userinpt[3] + " " + userinpt[4] + " " + userinpt[5] + " " + '|')
        print('|' + " " + userinpt[6] + " " + userinpt[7] + " " + userinpt[8] + " " + '|')
        print('---------')

    theBoard()
    check_win()

