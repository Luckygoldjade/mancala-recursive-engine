# Project Portfolio
# Author: Tony Chan
# GitHub username: Luckygoldjade
# Date: 12/4/22
# Description: Mancala game. To collect as many seeds in your store as possible.
# The player with the most seeds in his/her store at the end of the game wins.
#
# File: Mancala.py
# Instructor: Luyao Zhang, Doshna Reddy, Eric Muhati, Hannah Scott
# CS162 Fall 2022

# --
# Import Modules
# --
#import unittest

# --
# Class Definition
# --
class Mancala:
    """
    Mancala is a board game. The objective is to collect as many seeds in your store as possible.
    The player with the most seeds in his/her store at the end of the game wins.
    Responsibilities:   board is initialized with stores and pits
                        create player with name
                        rules enforcement
                        knows which player is playing game
                        how many seeds to move
                        add or subtract seeds from pits
                        tracks last seed moved
                        tracks empty pits
                        enforces special rules 1 and 2
                        print board for both players
                        print status of a player
                        determines if game is over
                        determine winner
                        tabulate scores
    Class to Class:     Mancala class can access Player class methods and members
                            can create Player object with name
                            can get Player names
                        Player class
                            cannot access Mancala methods and members
    """
    def __init__(self):
        self._board_lst = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self._player_1_board_lst = [1, 2, 3, 4, 5, 6]       # constant
        self._player_2_board_lst = [8, 9, 10, 11, 12, 13]   # constant
        self._player_1_store_num = 7                        # constant
        self._player_2_store_num = 14                       # constant
        self._player1 = None
        self._player2 = None


    def print_class_Mancala(self):
        """
        Purpose: Print Mancala class members
        Parameters: None
        Return:
        """
        print("==== start class Node ====")
        print("board= ", self._board_lst)
        print("player 1 board indices= ", self._player_1_board_lst)
        print("player 2 board indices= ", self._player_2_board_lst)
        print("player 1 store num index= ", self._player_1_store_num)
        print("player 2 store num index= ", self._player_2_store_num)
        print("==== end class Node ====")



    def print_board(self):
        """
        Purpose: Print the status and board for both players in a visually clear and beginner-friendly way
        """
        player_1_pits = [self._board_lst[i] for i in range(6)]
        player_2_pits = [self._board_lst[i] for i in range(7, 13)]
        store1 = self._board_lst[self._player_1_store_num-1]
        store2 = self._board_lst[self._player_2_store_num-1]
        print()
        print("================ MANCALA BOARD ================")
        print("This is the current state of the board:")
        print()
        if self._player2 is not None:
            print("Player 2 (" + str(self._player2._player_name) + ") side:")
        else:
            print("Player 2 side:")
        print("  Store:", store2)
        print("  Pits:  ", end="")
        for pit in reversed(player_2_pits):
            print(str(pit), end="  ")
        print()
        print("-----------------------------------------------")
        print("           ", end="")
        for pit in player_1_pits:
            print(str(pit), end="  ")
        print()
        if self._player1 is not None:
            print("Player 1 (" + str(self._player1._player_name) + ") side:")
        else:
            print("Player 1 side:")
        print("  Store:", store1)
        print("===============================================")
        print()

    def create_player(self, player_name, player_num=1):
        """
        Purpose: Create player instance with name member
        Parameters: player_name (str), player_num (1 or 2)
        Return: player instance object
        """
        player = Player(player_name)
        if player_num == 1:
            self._player1 = player
        elif player_num == 2:
            self._player2 = player
        return player

# --
    def play_game(self, player_index_num, pos):
        """
        Purpose:    Heart of the game.
                    create player with name
                    rules enforcement
                    knows which player is playing game
                    how many seeds to move
                    add or subtract seeds from pits
                    tracks last seed moved
                    tracks empty pits
                    enforces special rules 1 and 2
                    determines if game is over
        Parameters: two parameters, player number and pit number
        Return:     check pit number is out of range then return "Invalid number for pit index"
                    special rule 1 then print("player 1 take another turn")
                    special rule 1 then print("player 2 take another turn")
                    all pits are empty for a player then return "Game is ended"
                    last task for turn to be done then return one list of pits for both players
        """


        # check for valid pit index number
        if pos > 6 or pos <= 0:
            print()
            print("Oops! You tried to pick pit number " + str(pos) + ".")
            print("Please select a pit between 1 and 6.")
            print()
            return "Invalid number for pit index"


        if player_index_num == 2:
            pos = pos + 7
        if player_index_num == 1:
            if self._player1 is not None:
                print("Player 1 (" + str(self._player1._player_name) + ") is making a move from pit " + str(pos) + ".")
            else:
                print("Player 1 is making a move from pit " + str(pos) + ".")
        else:
            if self._player2 is not None:
                print("Player 2 (" + str(self._player2._player_name) + ") is making a move from pit " + str(pos-7) + ".")
            else:
                print("Player 2 is making a move from pit " + str(pos-7) + ".")

        next_pit_num = pos
        next_pit_num += 1
        return self.play_game_rec(player_index_num, next_pit_num, pos)

# --
    def play_game_rec(self, player_index_num, next_pit_num, pos):
        """
        helper for play game
        """
        if next_pit_num > 14:
            next_pit_num = 1

        # --
        # game over when one player pits are all empty
        # check both players
        player_1_all_pits_empty = True
        for pit_cnt1 in range(1, 7):
            if self._board_lst[pit_cnt1-1] != 0:
                player_1_all_pits_empty = False

        player_2_all_pits_empty = True
        for pit_cnt1 in range(8, 14):
            if self._board_lst[pit_cnt1-1] != 0:
                player_2_all_pits_empty = False

        if player_1_all_pits_empty == True or player_2_all_pits_empty == True:

            # clear pits and put in store
            # add up all the seeds in pits and store for each player
            # move seeds from pits to store
            # player 1
            for pit_cnt1 in range(1, 7):
                self._board_lst[self._player_1_store_num-1] = self._board_lst[self._player_1_store_num-1] + \
                                                              self._board_lst[pit_cnt1-1]
                self._board_lst[pit_cnt1-1] = 0         # clear pit
            # player 2
            for pit_cnt1 in range(8, 14):
                self._board_lst[self._player_2_store_num-1] = self._board_lst[self._player_2_store_num-1] + \
                                                              self._board_lst[pit_cnt1-1]
                self._board_lst[pit_cnt1-1] = 0         # clear pit

            return "Game is ended"




        # player 1
        if player_index_num == 1:
            # --
            # seed count != 1 (Not last seed and 0 seed) start
            if self._board_lst[pos-1] > 1:
                if next_pit_num == 14:                          # p1 skips p2 store
                    next_pit_num = 1
                # board index is always [pos-1]
                self._board_lst[pos-1] -= 1
                self._board_lst[next_pit_num-1] += 1
            # seed count != 1 (Not last seed) end



            # seed count = 1 (last seed) start
            elif self._board_lst[pos-1] == 1:
                if next_pit_num == self._player_1_store_num:    # player 1 store
                    # Special rule 1
                    if next_pit_num == 14:                      # p1 skips p2 store
                        next_pit_num = 1
                    # board index is always pos-1
                    self._board_lst[pos - 1] -= 1
                    self._board_lst[next_pit_num - 1] += 1
                    print()
                    print("Special Event!")
                    if self._player1 is not None:
                        print("Player 1 (" + str(self._player1._player_name) + ") gets another turn!")
                    else:
                        print("Player 1 gets another turn!")
                    print()
                    return self._board_lst

                elif next_pit_num in self._player_1_board_lst:  # player 1 pits
                    if self._board_lst[next_pit_num - 1] == 0:
                        # Special rule 2
                        print()
                        print("Special Event!")
                        if self._player1 is not None:
                            print("Player 1 (" + str(self._player1._player_name) + ") captures seeds from Player 2!")
                        else:
                            print("Player 1 captures seeds from Player 2!")
                        print()
                        self._board_lst[self._player_1_store_num-1] = self._board_lst[self._player_1_store_num-1] + \
                                                                    self._board_lst[self.oppo_plyr_1_pit_num(next_pit_num)-1]
                        # empty opponent's opposite pit
                        self._board_lst[self.oppo_plyr_1_pit_num(next_pit_num)-1] = 0

                        # add last seed to your store not to pit
                        self._board_lst[pos - 1] -= 1
                        self._board_lst[self._player_1_store_num - 1] += 1

                        return self._board_lst

                    elif self._board_lst[next_pit_num - 1] >= 1:
                        if next_pit_num == 14:                  # p1 skips p2 store
                            next_pit_num = 1
                        # board index is always pos-1
                        self._board_lst[pos - 1] -= 1
                        self._board_lst[next_pit_num - 1] += 1
                        return self._board_lst


                elif next_pit_num in self._player_2_board_lst:   # player 2 pits
                    #if self._board_lst[next_pit_num - 1] >= 1:
                    if next_pit_num == 14:                      # p1 skips p2 store
                        next_pit_num = 1
                    # board index is always pos-1
                    self._board_lst[pos - 1] -= 1
                    self._board_lst[next_pit_num - 1] += 1
                    return self._board_lst


                elif next_pit_num == self._player_2_store_num:   # player 2 store
                    #if self._board_lst[next_pit_num - 1] >= 1:
                    if next_pit_num == 14:                      # p1 skips p2 store
                        next_pit_num = 1



                    if next_pit_num in self._player_1_board_lst:  # player 1 pits
                        if self._board_lst[next_pit_num - 1] == 0:
                            # Special rule 2
                            # add opponent's opposite pit to your store
                            self._board_lst[self._player_1_store_num-1] = self._board_lst[self._player_1_store_num-1] + \
                                                                            self._board_lst[
                                                                                self.oppo_plyr_1_pit_num(next_pit_num)-1]
                            # empty opponent's opposite pit
                            self._board_lst[self.oppo_plyr_1_pit_num(next_pit_num)-1] = 0

                            # add last seed to your store not to pit
                            self._board_lst[pos - 1] -= 1
                            self._board_lst[self._player_1_store_num - 1] += 1

                            self.board_after_win()  # after game over clear board
                            return self._board_lst

                        elif self._board_lst[next_pit_num - 1] >= 1:
                            if next_pit_num == 14:  # p1 skips p2 store
                                next_pit_num = 1
                            # board index is always pos-1
                            self._board_lst[pos - 1] -= 1
                            self._board_lst[next_pit_num - 1] += 1
                            return self._board_lst

            # seed count = 1 (last seed) end


            # seed count <= 0 (0 seed) start
            elif self._board_lst[pos-1] <= 0:
                # do nothing. get next turn
                return self._board_lst

            # seed count <= 0 (0 seed) end

        # =======
        # player 2
        if player_index_num == 2:
            # --
            # seed count != 1 (Not last seed and 0 seed) start
            if self._board_lst[pos - 1] > 1:
                if next_pit_num == 7:                       # p2 skips p1 store
                    next_pit_num += 1
                # board index is always [pos-1]
                self._board_lst[pos - 1] -= 1
                self._board_lst[next_pit_num - 1] += 1
            # seed count != 1 (Not last seed) end

            # seed count = 1 (last seed) start
            elif self._board_lst[pos - 1] == 1:
                if next_pit_num == self._player_2_store_num:  # player 2 store
                    # Special rule 1
                    if next_pit_num == 7:                   # p2 skips p1 store
                        next_pit_num += 1
                    # board index is always pos-1
                    self._board_lst[pos - 1] -= 1
                    self._board_lst[next_pit_num - 1] += 1
                    print()
                    print("Special Event!")
                    if self._player2 is not None:
                        print("Player 2 (" + str(self._player2._player_name) + ") gets another turn!")
                    else:
                        print("Player 2 gets another turn!")
                    print()
                    return self._board_lst

                elif next_pit_num in self._player_2_board_lst:  # player 2 pits
                    if self._board_lst[next_pit_num - 1] == 0:
                        # Special rule 2
                        print()
                        print("Special Event!")
                        if self._player2 is not None:
                            print("Player 2 (" + str(self._player2._player_name) + ") captures seeds from Player 1!")
                        else:
                            print("Player 2 captures seeds from Player 1!")
                        print()
                        self._board_lst[self._player_2_store_num-1] = self._board_lst[self._player_2_store_num-1] + \
                                                                        self._board_lst[
                                                                            self.oppo_plyr_2_pit_num(next_pit_num)-1]
                        # empty opponent's opposite pit
                        self._board_lst[self.oppo_plyr_2_pit_num(next_pit_num)-1] = 0

                        # add last seed to your store not to pit
                        self._board_lst[pos - 1] -= 1
                        self._board_lst[self._player_2_store_num - 1] += 1

                        return self._board_lst
                    elif self._board_lst[next_pit_num - 1] >= 1:
                        if next_pit_num == 7:                      # p2 skips p1 store
                            next_pit_num += 1
                        # board index is always pos-1
                        self._board_lst[pos - 1] -= 1
                        self._board_lst[next_pit_num - 1] += 1
                        return self._board_lst


                elif next_pit_num in self._player_1_board_lst or \
                        next_pit_num == self._player_1_store_num:  # player 1 pits
                    # if self._board_lst[next_pit_num - 1] >= 1:
                    if next_pit_num == 7:                          # p2 skips p1 store
                        next_pit_num += 1
                    # board index is always pos-1
                    self._board_lst[pos - 1] -= 1
                    self._board_lst[next_pit_num - 1] += 1
                    return self._board_lst





                elif next_pit_num == self._player_1_store_num:  # player 1 store
                    # if self._board_lst[next_pit_num - 1] >= 1:
                    if next_pit_num == 7:                          # p2 skips p1 store
                        next_pit_num += 1



                    if next_pit_num in self._player_2_board_lst:  # player 2 pits
                        if self._board_lst[next_pit_num - 1] == 0:
                            # Special rule 2
                            # add opponent's opposite pit to your store
                            self._board_lst[self._player_2_store_num-1] = self._board_lst[self._player_2_store_num-1] + \
                                                                            self._board_lst[
                                                                                self.oppo_plyr_2_pit_num(next_pit_num)-1]
                            # empty opponent's opposite pit
                            self._board_lst[self.oppo_plyr_2_pit_num(next_pit_num)-1] = 0

                            # add last seed to your store not to pit
                            self._board_lst[pos - 1] -= 1
                            self._board_lst[self._player_2_store_num - 1] += 1

                            self.board_after_win()  # after game over clear board
                            return self._board_lst
                        elif self._board_lst[next_pit_num - 1] >= 1:
                            if next_pit_num == 7:                      # p2 skips p1 store
                                next_pit_num += 1
                            # board index is always pos-1
                            self._board_lst[pos - 1] -= 1
                            self._board_lst[next_pit_num - 1] += 1
                            return self._board_lst

            # seed count = 1 (last seed) end

            # seed count <= 0 (0 seed) start
            elif self._board_lst[pos - 1] <= 0:
                # do nothing. get next turn
                return self._board_lst

            # seed count <= 0 (0 seed) end

        # --
        next_pit_num += 1
        return self.play_game_rec(player_index_num, next_pit_num, pos)


# --
    def return_winner(self):
        """
        Purpose: Game over is not the same as winning. The store seeds are added up
                 and outcome is returned. It will access both board and add up seeds in
                 the players respective stores. It can be called at any time not just
                 after game over
        Parameters: None
        Return: Player 1 store seeds > Player 2 store seeds then return "Winner is player 1: ", player's name'
                Player 2 store seeds > Player 1 store seeds then return "Winner is player 2: ", player's name
                Player 1 store seeds = Player 2 store seeds then return "It's a tie"
                No player has all their pits empty then return "Game has not ended"
        """
        # only if game over
        # game has not ended. check both players
        player_1_all_pits_empty = True
        for pit_cnt1 in range(1, 7):
            if self._board_lst[pit_cnt1-1] != 0:
                player_1_all_pits_empty = False

        player_2_all_pits_empty = True
        for pit_cnt1 in range(8, 14):
            if self._board_lst[pit_cnt1-1] != 0:
                player_2_all_pits_empty = False

        if player_1_all_pits_empty == False and player_2_all_pits_empty == False:
            return "Game has not ended"

        player_1_score = self._board_lst[self._player_1_store_num-1]
        player_2_score = self._board_lst[self._player_2_store_num-1]
        if player_1_score > player_2_score:
            winner_name = self._player1._player_name if self._player1 else "Player 1"
            return "Winner is player 1: " + winner_name
        elif player_1_score < player_2_score:
            winner_name = self._player2._player_name if self._player2 else "Player 2"
            return "Winner is player 2: " + winner_name
        elif player_1_score == player_2_score:
            return "It's a tie"




# --
    def oppo_plyr_1_pit_num(self, player1_pit_num):
        """
        Purpose: Get player 2 pit number opposite to Player 1 pit number
        parameter: receives player 1 pit number
        returns: player 2 pit number opposite to player 1 pit number
        """
        # p1 pit6 -> p2 pit1
        if player1_pit_num == 1:
            return 13                    # p2 pit 6
        elif player1_pit_num == 2:
            return 12
        elif player1_pit_num == 3:
            return 11
        elif player1_pit_num == 4:
            return 10
        elif player1_pit_num == 5:
            return 9
        elif player1_pit_num == 6:
            return 8
        else:
            raise ValueError(f"Invalid player1_pit_num: {player1_pit_num}. Must be 1-6.")


# --
    def oppo_plyr_2_pit_num(self, player2_pit_num):
        """
        Purpose: Get player 1 pit number opposite to Player 2 pit number
        parameter: receives player 2 pit number
        returns: player 1 pit number opposite to player 2 pit number
        """
        # p1 pit6 -> p2 pit1
        if player2_pit_num == 8:        # p2 pit 8
            return 6
        elif player2_pit_num == 9:
            return 5
        elif player2_pit_num == 10:
            return 4
        elif player2_pit_num == 11:
            return 3
        elif player2_pit_num == 12:
            return 2
        elif player2_pit_num == 13:
            return 1
        else:
            raise ValueError(f"Invalid player2_pit_num: {player2_pit_num}. Must be 8-13.")


    def board_after_win(self):
        """
        Purpose: Checks if game is over and will update board. It will put all players'
        seeds in pits in players' store
        parameter: None
        returns: None
        """
        # --
        # game over when one player pits are all empty
        # check both players
        player_1_all_pits_empty = True
        for pit_cnt1 in range(1, 7):
            if self._board_lst[pit_cnt1-1] != 0:
                player_1_all_pits_empty = False

        player_2_all_pits_empty = True
        for pit_cnt1 in range(8, 14):
            if self._board_lst[pit_cnt1-1] != 0:
                player_2_all_pits_empty = False

        if player_1_all_pits_empty == True or player_2_all_pits_empty == True:

            # clear pits and put in store
            # add up all the seeds in pits and store for each player
            # move seeds from pits to store
            # player 1
            for pit_cnt1 in range(1, 7):
                self._board_lst[self._player_1_store_num-1] = self._board_lst[self._player_1_store_num-1] + \
                                                              self._board_lst[pit_cnt1-1]
                self._board_lst[pit_cnt1-1] = 0         # clear pit
            # player 2
            for pit_cnt1 in range(8, 14):
                self._board_lst[self._player_2_store_num-1] = self._board_lst[self._player_2_store_num-1] + \
                                                              self._board_lst[pit_cnt1-1]
                self._board_lst[pit_cnt1-1] = 0         # clear pit




class Player:
    """
    creates player object with member name
    Responsibilities:   stores name of player
                        There are only two players, 1 and 2
    Class to Class:     Mancala class can access Player methods and members
                            can get Player names
                            can create Player objects
                        Player class cannot access Mancala methods or members
    """
    def __init__(self, player_name):
        self._player_name = player_name



def get_player_name(self):
    """
    Purpose: Retrieve player name from member
    Parameters: None
    Return: return player name
    """
    return self._player_name


# =======
# Function Definition
# --













# --
# main start
def main():
    """

    """
    # --
    # Class Instantiation
    # --
    # user Input and Output
    #
    # --
    # -- test
    # [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    # game = Mancala()
    # player1 = game.create_player("Lily")
    # player2 = game.create_player("Lucy")
    #print(type(player1))
    #print(player1)
    #game.print_board()
    #game.print_class_Mancala()

    #plyr1 default
    # === Screenshot 1: Game Start ===
    print()
    print("================ WELCOME TO MANCALA! ================")
    print("Welcome to the classic game of Mancala!")
    print("Your goal is to collect as many seeds in your store as possible.")
    print("Player 1: Lily   Player 2: Lucy")
    print("Let's begin! Good luck to both players!")
    print("====================================================")
    print()
    game = Mancala()
    player1 = game.create_player("Lily", 1)
    player2 = game.create_player("Lucy", 2)
    game.print_board()

    # === Screenshot 2: Player 1 Move ===
    print("It's Player 1's turn. Lily will make a move from pit 3.")
    game.play_game(1, 3)
    game.print_board()

    # === Screenshot 3: Player 2 Move ===
    print("Now it's Player 2's turn. Lucy will make a move from pit 4.")
    game.play_game(2, 4)
    game.print_board()

    # === Screenshot 4: Special Event (Player 1 gets another turn or capture) ===
    print("Watch for a special event! Lily (Player 1) will make a move from pit 6.")
    game.play_game(1, 6)
    game.print_board()

    # === Screenshot 5: Game Over ===
    print("Let's fast-forward to the end of the game for demonstration.")
    # Manually set up a nearly finished board for screenshot
    game._board_lst = [0, 0, 0, 0, 0, 1, 20, 0, 0, 0, 0, 0, 1, 18]
    game.print_board()
    print("Game over! Let's see who won.")
    print(game.return_winner())
    # game.print_class_Mancala()




    # plyr1 add seeds to p2 pits
    # [2, 2, 0, 2, 4, 1, 0, 2, 2, 2, 2, 2, 2, 0]
    # game.play_game(1, 5)
    # game.print_board()
    # game.print_class_Mancala()

    # plyr1 wrap around to p2 12 pits + 1 store
    # [2, 2, 0, 2, 10, 1, 0, 2, 2, 2, 2, 2, 2, 0]
    # game.play_game(1, 5)
    # game.print_board()
    # game.print_class_Mancala()


    # plyr2 game over
    # [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0]
    # print(game.play_game(2, 3))
    # game.print_board()
    # game.print_class_Mancala()


    # plyr1 invalid pit num
    # [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0]
    # print(game.play_game(1, 9))
    # game.print_board()
    # game.print_class_Mancala()

    # plyr2 game has not ended
    # [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
    # [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1]
    # print(game.return_winner())
    # game.print_board()

    # ply2 game has ended
    # [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
    # [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1]
    # print(game.return_winner())
    # game.print_board()






    # =======


    # game = Mancala()
    # player1 = game.create_player("Lily")
    # player2 = game.create_player("Lucy")
    # print(game.play_game(1, 3))
    # print(game.play_game(1, 1))
    # print(game.play_game(2, 3))
    # print(game.play_game(2, 4))
    # print(game.play_game(1, 2))
    # print(game.play_game(2, 2))
    # print(game.play_game(1, 1))
    # game.print_board()
    # print(game.return_winner())




    # --
    # -- test
    game = Mancala()
    game.print_board()
    game.print_class_Mancala
    playerl = game.create_player("Lily")
    player2 = game.create_player("Lucy")
    print(game.play_game(1, 1))
    print(game.play_game(1, 2))
    print(game.play_game(1, 3))
    print(game.play_game(1, 4))
    print(game.play_game(1, 5))
    print(game.play_game(1, 6))
    game.print_board()
    game.print_class_Mancala()
    print(game.return_winner())

    game.print_board()



    # --
    # -- test
    # game = Mancala()
    # playerl = game.create_player("Lily")
    # player2 = game.create_player("Lucy")
    # print(game.play_game(2, 1))
    # print(game.play_game(2, 2))
    # print(game.play_game(2, 3))
    # print(game.play_game(2, 4))
    # print(game.play_game(2, 5))
    # print(game.play_game(2, 6))
    # game.print_board()
    # print(game.return_winner())

    # game.print_board()



    # --
    # -- test



    # --
    # -- test




    # --
    # end main
if __name__ == '__main__':
    main()
