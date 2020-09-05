import math
import sys

list_1 = [0,0,0]
list_2 = [0,0,0]
list_3 = [0,0,0]

board = [
            list_1,
            list_2,
            list_3
        ]

non_zero_list = []
groove = []
alarm = 0

print("\n~ Instruction ~\n")

print("(1) Player-1 gets ODD numbers b/w 1 to 9 (i.e. 1, 3, 5, 7, 9),")
print("(2) Player-2 gets EVEN numbers b/w 1 to 9 (i.e. 2, 4, 6, 8),")
print("(3) The player who's three number sum is 15 wins,")
print("(4) Each player will get alternative turn to enter number,")
print("If you enter used/invalid number you will lost your turn,")
print("(5) The number can't be repeated,")
print("(6) First enter your desired tile number between 1 to 9,")
print("(7) Then your number,")
print("(8)The game will go-on until unless one player wins or all the players allotted numbers are used.")
print("(9) Enter Ctrl+C to exit the game!\n")
print("All the best, may the 15 be with you! :D")

print("\n~ Board ~\n")
for item in board:
    print(item)

while True: 

    def player_1_move():
        global player_1_tile, player_1_odd
        player_1_tile = int(input("\n(Odd) Player - 1: ENTER TILE NUMBER >> ").strip())
        player_1_odd = int(input("(Odd) Player - 1: ENTER ODD NUMBER >> ").strip())
        print("\n")

        for item in board:
            for tile in item:
                if tile == player_1_odd:
                    print("Pls enter number which is not used before! You lost your turn!\n")
                    player_2_move()

        if player_1_odd == 1:

            if player_1_tile <= 3 and player_1_tile >= 1:
                player_1_tile = player_1_tile -1
                if list_1[player_1_tile] == 0:
                    list_1[player_1_tile] = player_1_odd
                    #print("Working 1")
                    print("\n~ Board ~\n")
                    for item in board:
                        print(item)
                    #print("\n")
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 3 and player_1_tile <= 6:
                player_1_tile = player_1_tile -4
                if list_2[player_1_tile] == 0:
                    list_2[player_1_tile] = player_1_odd
                    #print("Working 3")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 6 and player_1_tile <= 9:
                player_1_tile = player_1_tile -7
                if list_3[player_1_tile] == 0:
                    list_3[player_1_tile] = player_1_odd
                    #print("Working 9")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")


        elif player_1_odd == 3:

            if player_1_tile <= 3 and player_1_tile >= 1:
                player_1_tile = player_1_tile -1
                if list_1[player_1_tile] == 0:
                    list_1[player_1_tile] = player_1_odd
                    #print("Working 1")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 3 and player_1_tile <= 6:
                player_1_tile = player_1_tile -4
                if list_2[player_1_tile] == 0:
                    list_2[player_1_tile] = player_1_odd
                    #print("Working 3")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 6 and player_1_tile <= 9:
                player_1_tile = player_1_tile -7
                if list_3[player_1_tile] == 0:
                    list_3[player_1_tile] = player_1_odd
                    #print("Working 9")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")


        elif player_1_odd == 5:

            if player_1_tile <= 3 and player_1_tile >= 1:
                player_1_tile = player_1_tile -1
                if list_1[player_1_tile] == 0:
                    list_1[player_1_tile] = player_1_odd
                    #print("Working 1")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 3 and player_1_tile <= 6:
                player_1_tile = player_1_tile -4
                if list_2[player_1_tile] == 0:
                    list_2[player_1_tile] = player_1_odd
                    #print("Working 3")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 6 and player_1_tile <= 9:
                player_1_tile = player_1_tile -7
                if list_3[player_1_tile] == 0:
                    list_3[player_1_tile] = player_1_odd
                    #print("Working 9")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")


        elif player_1_odd == 7:

            if player_1_tile <= 3 and player_1_tile >= 1:
                player_1_tile = player_1_tile -1
                if list_1[player_1_tile] == 0:
                    list_1[player_1_tile] = player_1_odd
                    #print("Working 1")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 3 and player_1_tile <= 6:
                player_1_tile = player_1_tile -4
                if list_2[player_1_tile] == 0:
                    list_2[player_1_tile] = player_1_odd
                    #print("Working 3")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 6 and player_1_tile <= 9:
                player_1_tile = player_1_tile -7
                if list_3[player_1_tile] == 0:
                    list_3[player_1_tile] = player_1_odd
                    #print("Working 9")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")


        elif player_1_odd == 9:

            if player_1_tile <= 3 and player_1_tile >= 1:
                player_1_tile = player_1_tile -1
                if list_1[player_1_tile] == 0:
                    list_1[player_1_tile] = player_1_odd
                    #print("Working 3")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 3 and player_1_tile <= 6:
                player_1_tile = player_1_tile -4
                if list_2[player_1_tile] == 0:
                    list_2[player_1_tile] = player_1_odd
                    #print("Working 5")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_1_tile >= 6 and player_1_tile <= 9:
                player_1_tile = player_1_tile -7
                if list_3[player_1_tile] == 0:
                    list_3[player_1_tile] = player_1_odd
                    #print("Working 9")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

        elif player_1_odd == 2 or player_1_odd == 4 or player_1_odd == 6 or player_1_odd == 8:
            print("Oops, you entered even number, you lost your turn!")
            for item in board:
                print(item)

        else:
            print("Oops, your entered number is invalid, you lost your turn!")
            for item in board:
                print(item)

            
    def player_2_move():
        global player_2_tile, player_2_even
        player_2_tile = int(input("\n(Even) Player - 2: ENTER TILE NUMBER >> ").strip())
        player_2_even = int(input("(Even) Player - 2: ENTER EVEN NUMBER >> ").strip())
        print("\n")

        for item in board:
            for tile in item:
                if tile == player_2_even:
                    print("Pls enter number which is not used before! You lost your turn!")
                    player_1_move()

        if player_2_even == 2:

            if player_2_tile <= 3 and player_2_tile >= 1:
                player_2_tile = player_2_tile -1
                if list_1[player_2_tile] == 0:
                    list_1[player_2_tile] = player_2_even
                    #print("Working 1")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

            elif player_2_tile >= 3 and player_2_tile <= 6:
                player_2_tile = player_2_tile -4
                if list_2[player_2_tile] == 0:
                    list_2[player_2_tile] = player_2_even
                    #print("Working 3")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

            elif player_2_tile >= 6 and player_2_tile <= 9:
                player_2_tile = player_2_tile -7
                if list_3[player_2_tile] == 0:
                    list_3[player_2_tile] = player_2_even
                    #print("Working 9")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

        elif player_2_even == 4:

            if player_2_tile <= 3 and player_2_tile >= 1:
                player_2_tile = player_2_tile -1
                if list_1[player_2_tile] == 0:
                    list_1[player_2_tile] = player_2_even
                    #print("Working 1")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

            elif player_2_tile >= 3 and player_2_tile <= 6:
                player_2_tile = player_2_tile -4
                if list_2[player_2_tile] == 0:
                    list_2[player_2_tile] = player_2_even
                    #print("Working 3")
                    for item in board:
                        print(item)
                else:
                    print("Enter Un-used number!")

            elif player_2_tile >= 6 and player_2_tile <= 9:
                player_2_tile = player_2_tile -7
                if list_3[player_2_tile] == 0:
                    list_3[player_2_tile] = player_2_even
                    #print("Working 9")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

        elif player_2_even == 6:

            if player_2_tile <= 3 and player_2_tile >= 1:
                player_2_tile = player_2_tile -1
                if list_1[player_2_tile] == 0:
                    list_1[player_2_tile] = player_2_even
                    #print("Working 1")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

            elif player_2_tile >= 3 and player_2_tile <= 6:
                player_2_tile = player_2_tile -4
                if list_2[player_2_tile] == 0:
                    list_2[player_2_tile] = player_2_even
                    #print("Working 3")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

            elif player_2_tile >= 6 and player_2_tile <= 9:
                player_2_tile = player_2_tile -7
                if list_3[player_2_tile] == 0:
                    list_3[player_2_tile] = player_2_even
                    #print("Working 9")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

        elif player_2_even == 8:

            if player_2_tile <= 3 and player_2_tile >= 1:
                player_2_tile = player_2_tile -1
                if list_1[player_2_tile] == 0:
                    list_1[player_2_tile] = player_2_even
                    #print("Working 1")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

            elif player_2_tile >= 3 and player_2_tile <= 6:
                player_2_tile = player_2_tile -4
                if list_2[player_2_tile] == 0:
                    list_2[player_2_tile] = player_2_even
                    #print("Working 3")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()

            elif player_2_tile >= 6 and player_2_tile <= 9:
                player_2_tile = player_2_tile -7
                if list_3[player_2_tile] == 0:
                    list_3[player_2_tile] = player_2_even
                    #print("Working 9")
                    for item in board:
                        print(item)
                else:
                    print("Enter number in empty tile only! You lost your turn!")
                    player_1_move()
        
        elif player_1_odd == 1 or player_1_odd == 3 or player_1_odd == 5 or player_1_odd == 7 or player_1_odd == 7:
            print("Oops, you entered odd number, you lost your turn!")

        else:
            print("Oops, your entered number is invalid, you lost your turn!")

    def bingo_algo(winner):
        if sum(list_1) == 15 and list_1[0] != 0 and list_1[1] != 0 and list_1[2] != 0:
            print(winner)
            sys.exit()

        elif sum(list_2) == 15 and list_2[0] != 0 and list_2[0] != 0 and list_2[0] != 0:
            print(winner)
            sys.exit()

        elif sum(list_3) == 15 and list_3[0] != 0 and list_3[0] != 0 and list_3[0] != 0:
            print(winner)
            sys.exit()
        
        elif list_1[0] + list_2[0] + list_3[0] == 15 and list_1[0] != 0 and list_2[0] != 0 and list_3[0] != 0:
            print(winner)
            sys.exit()

        elif list_1[1] + list_2[1] + list_3[1] == 15 and list_1[1] != 0 and list_2[2] != 0 and list_3[1] != 0:
            print(winner)
            sys.exit()

        elif list_1[2] + list_2[2] + list_3[2] == 15 and list_1[2] != 0 and list_2[2] != 0 and list_3[2] != 0:
            print(winner)
            sys.exit()

        elif list_1[0] + list_2[1] + list_3[2] == 15 and list_1[0] != 0 and list_2[1] != 0 and list_3[2] != 0:
            print(winner)
            sys.exit()

        elif list_1[2] + list_2[1] + list_3[0] == 15 and list_1[2] != 0 and list_2[1] != 0 and list_3[0] != 0:
            print(winner)
            sys.exit()

    def no_winner():
        for lists in board:
            for tiles in lists:
                groove.append(tiles)
        for item in groove:
            if item != 0:
                non_zero_list.append(tiles)
                alarm = 1

        if alarm == 1 and len(non_zero_list) == 9:
            print("\n TIE! TIE!! TIE!!!")
            sys.exit()

    player_1_move()
    bingo_algo("\nPlayer-1 Wins!\n")
    no_winner()
    player_2_move()
    bingo_algo("\nPlayer-2 Wins!\n")
    no_winner()