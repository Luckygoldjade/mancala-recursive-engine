# Project Portfolio
# Author: Tony Chan
# GitHub username: Luckygoldjade
# Date: 11/29/22
# Description: Mancala game.
#
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
        self._board_lst = [2, 2, 0, 2, 10, 1, 0, 2, 2, 2, 2, 2, 2, 0]
        self._player_1_board_lst = [1, 2, 3, 4, 5, 6]       # constant
        self._player_2_board_lst = [8, 9, 10, 11, 12, 13]   # constant
        self._player_1_store_num = 7                        # constant
        self._player_2_store_num = 14                       # constant



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
        Purpose: Print the status and board for both players
        Parameters: None
        Return: Print the status and board for both players
        """
        player_1_pits_lst = []
        player_2_pits_lst = []

        print("player1:")
        print("store:", self._board_lst[self._player_1_store_num-1])
        # print player 1 pit 1 to 6
        for pit_cnt1 in range(0, 6):
            player_1_pits_lst.append(self._board_lst[pit_cnt1])

        print(player_1_pits_lst)

        print("player2:")
        print("store:", self._board_lst[self._player_2_store_num-1])
        # print player 2 pit 8 to 13
        for pit_cnt1 in range(7, 13):
            player_2_pits_lst.append(self._board_lst[pit_cnt1])

        print(player_2_pits_lst)

    def create_player(self, player_name):
        """
        Purpose: Create player instance with name member
        Parameters: one parameter for name
        Return: player instance object
        """
        player = Player(player_name)
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

        is_game_over = False
        # 1 for player 1, 2 for player 2

        # check for valid pit index number
        if pos > 6 and pos <= 0:
            return "Invalid number for pit index"





        next_pit_num = pos
        next_pit_num += 1
        self.play_game_rec(player_index_num, next_pit_num, pos)

# --
    def play_game_rec(self, player_index_num, next_pit_num, pos):
        """
        helper for play game
        """
        if next_pit_num >= 15:
            next_pit_num = 1

        # --
        if player_index_num == 1:
            # skip player 2 store
            skip_store_num = self._player_2_store_num
        else:
            # skip player 1 store
            skip_store_num = self._player_1_store_num

        # --
        # seed count != 1 (Not last seed and 0 seed) start
        if self._board_lst[pos-1] > 1:
            if next_pit_num == skip_store_num:
                next_pit_num += 1
            # board index is always [pos-1]
            self._board_lst[pos-1] -= 1
            self._board_lst[next_pit_num-1] += 1
        # seed count != 1 (Not last seed) end



        # seed count = 1 (last seed) start
        elif self._board_lst[pos-1] == 1:
            if next_pit_num == self._player_1_store_num:                   # player 1 store
                # Special rule 1
                if next_pit_num == skip_store_num:
                    next_pit_num += 1
                # board index is always pos-1
                self._board_lst[pos - 1] -= 1
                self._board_lst[next_pit_num - 1] += 1
                print("player 1 take another turn")
                return

            elif next_pit_num in self._player_1_board_lst:      # player 1 pits
                if self._board_lst[next_pit_num - 1] == 0:
                    # Special rule 2
                    print(True)
                    # add opponent's opposite pit to your store
                    self._board_lst[self._player_1_store_num-1] = self._board_lst[self._player_1_store_num-1] + \
                                                                self._board_lst[self.opposite_pit_num(next_pit_num+2)]
                    # empty opponent's opposite pit
                    self._board_lst[self.opposite_pit_num(next_pit_num+2)] = 0

                    # add last seed to your store not to pit
                    self._board_lst[pos - 1] -= 1
                    self._board_lst[self._player_1_store_num - 1] += 1



                    return
                elif self._board_lst[next_pit_num - 1] >= 1:
                    if next_pit_num == skip_store_num:
                        next_pit_num += 1
                    # board index is always pos-1
                    self._board_lst[pos - 1] -= 1
                    self._board_lst[next_pit_num - 1] += 1
                    return


            elif next_pit_num in self._player_2_board_lst or next_pit_num == self._player_2_store_num:    # player 2 pits and store
                #if self._board_lst[next_pit_num - 1] >= 1:
                if next_pit_num == skip_store_num:
                    next_pit_num += 1
                # board index is always pos-1
                self._board_lst[pos - 1] -= 1
                self._board_lst[next_pit_num - 1] += 1
                return

        # seed count = 1 (last seed) end


        # seed count <= 0 (0 seed) start
        elif self._board_lst[pos-1] <= 0:
            # do nothing. get next turn
            return

        # seed count <= 0 (0 seed) end






            #
            #     print("player 2 take another turn")

        # --
        next_pit_num += 1
        self.play_game_rec(player_index_num, next_pit_num, pos)

# --






        
        
        # # Fix*** may need to also check even before starting
        #
        # # game over is check player pits are all empty
        # # always check after move
        # if player_index_num == 1:
        #     player_1_all_pits_empty = True
        #     for pit_cnt1 in range(0, 5):
        #         if self._player_1_board_lst[pos] != 0:
        #             player_1_all_pits_empty = False
        #             return "Game is ended"
        # else:
        #     player_2_all_pits_empty = True
        #     for pit_cnt1 in range(0, 5):
        #         if self._player_2_board_lst[pos] != 0:
        #             player_2_all_pits_empty = False
        #             return "Game is ended"
        #
        #






        # add up score
        # always check after game over
        #


        # return 14 element list of board
        # return self._board_lst

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

        # if game over then count score:
        #     return "Winner is player 1: ", player's name'
        #
        #     return "Winner is player 2: ", player's name
        #
        # elif game is tie:
        #     return "It's a tie"
        #
        # if game is not over:
        #     return "Game has not ended"

# --
    def opposite_pit_num(self, player1_pit_num):
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


# --







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
        self.player_name = player_name



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
    game = Mancala()
    player1 = game.create_player("Lily")
    player2 = game.create_player("Lucy")
    #print(type(player1))
    #print(player1)
    game.print_board()
    game.print_class_Mancala()

    # p1 SR 1
    # [2, 2, 0, 2, 2, 1, 0, 2, 2, 2, 2, 2, 2, 0]
    # game.play_game(1, 6)
    # game.play_game(1, 6)
    # game.print_board()
    # game.print_class_Mancala()

    # p1 SR 1
    # [2, 2, 0, 2, 2, 1, 0, 2, 2, 2, 2, 2, 2, 0]
    # game.play_game(1, 5)
    # game.print_board()
    # game.print_class_Mancala()

    # p1 select empty pit
    # [2, 2, 0, 2, 2, 1, 0, 2, 2, 2, 2, 2, 2, 0]
    # game.play_game(1, 3)
    # game.print_board()
    # game.print_class_Mancala()


    # p1 SR 2
    # [2, 2, 0, 2, 2, 1, 0, 2, 2, 2, 2, 2, 2, 0]
    # game.play_game(1, 1)
    # game.play_game(1, 1)
    # game.print_board()
    # game.print_class_Mancala()


    # p1 add seeds to p2 pits
    # [2, 2, 0, 2, 4, 1, 0, 2, 2, 2, 2, 2, 2, 0]
    # game.play_game(1, 5)
    # game.print_board()
    # game.print_class_Mancala()

    # p1 wrap around to p2 12 pits + 1 store
    # [2, 2, 0, 2, 10, 1, 0, 2, 2, 2, 2, 2, 2, 0]
    game.play_game(1, 5)
    game.print_board()
    game.print_class_Mancala()


    # last select seed to p2 pits

    #player2 = game.create_player("Lucy")
    # test SR 2
    #print(game.play_game(1, 3))
    #game.print_class_Mancala()


    # game.play_game(1, 1)
    # game.play_game(2, 3)
    # game.play_game(2, 4)
    # game.play_game(1, 2)
    # game.play_game(2, 2)
    # game.play_game(1, 1)
    # game.print_board()
    #print(game.return_winner())




    # --
    # -- test
    # game = Mancala()
    # playerl = game.create_player("Lily")
    # player2 = game.create_player("Lucy")
    # game.play_game(1, 1)
    # game.play_game(1, 2)
    # game.play_game(1, 3)
    # game.play_game(1, 4)
    # game.play_game(1, 5)
    # game.play_game(1, 6)
    # game.print_board()
    # print(game.return_winner())



    # --
    # -- test



    # --
    # -- test



    # --
    # -- test




    # --
    # end main
if __name__ == '__main__':
    main()
