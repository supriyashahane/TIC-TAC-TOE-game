import os
import random
#os.system("clear")



class Board():
    def __init__(self):
        self.blocks = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print("\t\t\t\t ===============")
        print ("\t\t\t\t || %s | %s | %s ||" %(self.blocks[0], self.blocks[1], self.blocks[2]))
        print("\t\t\t\t ===============")
        print ("\t\t\t\t || %s | %s | %s ||" %(self.blocks[3], self.blocks[4], self.blocks[5]))
        print("\t\t\t\t ===============")
        print ("\t\t\t\t || %s | %s | %s ||" %(self.blocks[6], self.blocks[7], self.blocks[8]))
        print("\t\t\t\t ===============")


    def update_blocks(self, x_player, player):
        try:
            if self.blocks[x_player] == " ":
                self.blocks[x_player] = player
            elif player == "X":
                x_player = int(raw_input("\nblock is not empty Please chosse 0-8 > ") )
                self.update_blocks(x_player, player)
            else:
                self.ai_move(x_player)
        except IndexError:
            x_player = int(raw_input("\nblock is not empty Please chosse 0-8 > ") )
            self.update_blocks(x_player, player)

    def winner_player(self, player):
        if self.blocks[0] == player and self.blocks[1] == player and self.blocks[2] == player:
            return True
        if self.blocks[3] == player and self.blocks[4] == player and self.blocks[5] == player:
            return True
        if self.blocks[6] == player and self.blocks[7] == player and self.blocks[8] == player:
            return True
        if self.blocks[0] == player and self.blocks[3] == player and self.blocks[6] == player:
            return True
        if self.blocks[1] == player and self.blocks[4] == player and self.blocks[7] == player:
            return True
        if self.blocks[2] == player and self.blocks[5] == player and self.blocks[8] == player:
            return True
        if self.blocks[0] == player and self.blocks[4] == player and self.blocks[8] == player:
            return True
        if self.blocks[2] == player and self.blocks[4] == player and self.blocks[6] == player:
            return True
        return False
    def tie_found(self):
        used_blocks = 0
        for block in self.blocks:
            if block != " ":
                used_blocks += 1
        if used_blocks == 9:
            return True
        else:
            return False
    
    def reset(self):
        self.blocks = []
        self.blocks = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    
### Inheritance Concept
class player_show(Board):
    def __init__(self, name, class_a):
        self.name = name
        self.blocks = class_a.blocks
        #Board.__init__(self)
            
    ####Polymorphism
    def update_blocks(self, x_player, player):
        if self.blocks[x_player] == " ":
            self.blocks[x_player] = player
        elif player != "":
            x_player = int(raw_input("\nblock is not empty Please chosse 0-8 > ") )
            self.update_blocks(x_player, player)
        

    def player_move(self,player):
        print("player {} is".format( self.name))
        refresh_screen()
        x_player = raw_input("\n{} Please chosse 0-8 > ".format(self.name))
        if x_player in ["0","1","2","3","4","5","6","7","8"]:
            self.update_blocks(int(x_player), player)
            refresh_screen()
        elif x_player not in ["0","1","2","3","4","5","6","7","8"]:
            print("Incorrecr")
            self.player_move(player)

#### Inheritance Concept AI_Build
class ai_build(Board):
    def __init__(self, name, class_a):
        self.name = name
        self.blocks = class_a.blocks

    def ai_move(self, player):
        #cnt = cnt + 1
        #if player == "X":
         #   enemy = "O"
        #if player == "O":
         #   enemy = "X"
        #choose center
        if self.blocks[4] == " ":
            self.update_blocks(4, player)
        else:
            for i in range(0,8):
                
                #print(cnt)
                i = random.randint(0, 8)
                if self.blocks[i] == " ":
                    self.update_blocks(i, player)
                    #self.ai_move_sucess(player)
                    break
                
    
        #AI win player
    
    def ai_move_sucess(self, player):
        enemy = "X"
        if self.blocks[0] == player and self.blocks[3] == player and self.blocks[6] == " ":
            board.update_blocks(6, "O")
            #return 6
        elif self.blocks[3] == player and self.blocks[6] == player and self.blocks[0] == " ":
            board.update_blocks(0, "O")
            #return 0 
        elif self.blocks[0] == player and self.blocks[6] == player and self.blocks[3] == " ":
            board.update_blocks(3, "O")
            #return 3 

        elif self.blocks[1] == player and self.blocks[4] == player and self.blocks[7] == " ":
            board.update_blocks(7, "O")
            #return 7
        elif self.blocks[4] == player and self.blocks[7] == player and self.blocks[1] == " ":
            board.update_blocks(1, "O")
            #return 1
        elif self.blocks[7] == player and self.blocks[1] == player and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4

        elif self.blocks[2] == player and self.blocks[5] == player and self.blocks[8] == " ":
            board.update_blocks(8, "O")
            #return 8
        elif self.blocks[5] == player and self.blocks[8] == player and self.blocks[2] == " ":
            board.update_blocks(2, "O")#
            #return 2 
        elif self.blocks[8] == player and self.blocks[2] == player and self.blocks[5] == " ":
            board.update_blocks(5, "O")
            #return 5

        elif self.blocks[0] == player and self.blocks[1] == player and self.blocks[2] == " ":
            board.update_blocks(2, "O")
            #return 2
        elif self.blocks[1] == player and self.blocks[2] == player and self.blocks[0] == " ":
            board.update_blocks(0, "O")
            #return 0
        elif self.blocks[2] == player and self.blocks[0] == player and self.blocks[1] == " ":
            board.update_blocks(1, "O")
            #return 1

        elif self.blocks[3] == player and self.blocks[4] == player and self.blocks[5] == " ":
            board.update_blocks(5, "O")
            #return 5
        elif self.blocks[4] == player and self.blocks[5] == player and self.blocks[3] == " ":
            board.update_blocks(3, "O")
            #return 3
        elif self.blocks[5] == player and self.blocks[3] == player and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4
        
        elif self.blocks[6] == player and self.blocks[7] == player and self.blocks[8] == " ":
            board.update_blocks(8, "O")
            #return 8
        elif self.blocks[7] == player and self.blocks[8] == player and self.blocks[6] == " ":
            board.update_blocks(6, "O")
            #return 6
        elif self.blocks[8] == player and self.blocks[6] == player and self.blocks[7] == " ":
            board.update_blocks(7, "O")
            #return 7

        elif self.blocks[0] == player and self.blocks[4] == player and self.blocks[8] == " ":
            board.update_blocks(8, "O")
            #return 8
        elif self.blocks[4] == player and self.blocks[8] == player and self.blocks[0] == " ":
            board.update_blocks(0, "O")
            #return 0
        elif self.blocks[8] == player and self.blocks[0] == player and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4
        
        elif self.blocks[2] == player and self.blocks[4] == player and self.blocks[6] == " ":
            board.update_blocks(6, "O")
            #return 6
        elif self.blocks[4] == player and self.blocks[6] == player and self.blocks[2] == " ":
            board.update_blocks(2, "O")
            #return 2 
        elif self.blocks[6] == player and self.blocks[2] == player and self.blocks[4] == " ":
            board.update_blocks(4, "O")

        elif self.blocks[0] == enemy and self.blocks[3] == enemy and self.blocks[6] == " ":
            board.update_blocks(6, "O")
            #return 6
        elif self.blocks[3] == enemy and self.blocks[6] == enemy and self.blocks[0] == " ":
            board.update_blocks(0, "O")
            #return 0 
        elif self.blocks[0] == enemy and self.blocks[6] == enemy and self.blocks[3] == " ":
            board.update_blocks(3, "O")
            #return 3 

        elif self.blocks[1] == enemy and self.blocks[4] == enemy and self.blocks[7] == " ":
            board.update_blocks(7, "O")
            #return 7
        elif self.blocks[4] == enemy and self.blocks[7] == enemy and self.blocks[1] == " ":
            board.update_blocks(1, "O")
            #return 1
        elif self.blocks[7] == enemy and self.blocks[1] == enemy and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4

        elif self.blocks[2] == enemy and self.blocks[5] == enemy and self.blocks[8] == " ":
            board.update_blocks(8, "O")
            #return 8
        elif self.blocks[5] == enemy and self.blocks[8] == enemy and self.blocks[2] == " ":
            board.update_blocks(2, "O")
            #return 2 
        elif self.blocks[8] == enemy and self.blocks[2] == enemy and self.blocks[5] == " ":
            board.update_blocks(5, "O")
            #return 5

        elif self.blocks[0] == enemy and self.blocks[1] == enemy and self.blocks[2] == " ":
            board.update_blocks(2, "O")
            #return 2
        elif self.blocks[1] == enemy and self.blocks[2] == enemy and self.blocks[0] == " ":
            board.update_blocks(0, "O")
            #return 0
        elif self.blocks[2] == enemy and self.blocks[0] == enemy and self.blocks[1] == " ":
            board.update_blocks(1, "O")
            #return 1

        elif self.blocks[3] == enemy and self.blocks[4] == enemy and self.blocks[5] == " ":
            board.update_blocks(5, "O")
            #return 5
        elif self.blocks[4] == enemy and self.blocks[5] == enemy and self.blocks[3] == " ":
            board.update_blocks(3, "O")
            #return 3
        elif self.blocks[5] == enemy and self.blocks[3] == enemy and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4
        
        elif self.blocks[6] == enemy and self.blocks[7] == enemy and self.blocks[8] == " ":
            board.update_blocks(8, "O")
            #return 8
        elif self.blocks[7] == enemy and self.blocks[8] == enemy and self.blocks[6] == " ":
            board.update_blocks(6, "O")
            #return 6
        elif self.blocks[8] == enemy and self.blocks[6] == enemy and self.blocks[7] == " ":
            board.update_blocks(7, "O")
            #return 7

        elif self.blocks[0] == enemy and self.blocks[4] == enemy and self.blocks[8] == " ":
            board.update_blocks(8, "O")
            #return 8
        elif self.blocks[4] == enemy and self.blocks[8] == enemy and self.blocks[0] == " ":
            board.update_blocks(0, "O")
            #return 0
        elif self.blocks[8] == enemy and self.blocks[0] == enemy and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4
        
        elif self.blocks[2] == enemy and self.blocks[4] == enemy and self.blocks[6] == " ":
            board.update_blocks(6, "O")
            #return 6
        elif self.blocks[4] == enemy and self.blocks[6] == enemy and self.blocks[2] == " ":
            board.update_blocks(2, "O")
            #return 2 
        elif self.blocks[6] == enemy and self.blocks[2] == enemy and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4
        else :
            self.ai_move("O")

        #choose random
    
    
    def ai_move_sucess1(self, player):
        if self.blocks[0] == player and self.blocks[3] == player and self.blocks[6] == " ":
            board.update_blocks(6, "O")
            #return 6
        elif self.blocks[3] == player and self.blocks[6] == player and self.blocks[0] == " ":
            board.update_blocks(0, "O")
            #return 0 
        elif self.blocks[0] == player and self.blocks[6] == player and self.blocks[3] == " ":
            board.update_blocks(3, "O")
            #return 3 

        elif self.blocks[1] == player and self.blocks[4] == player and self.blocks[7] == " ":
            board.update_blocks(7, "O")
            #return 7
        elif self.blocks[4] == player and self.blocks[7] == player and self.blocks[1] == " ":
            board.update_blocks(1, "O")
            #return 1
        elif self.blocks[7] == player and self.blocks[1] == player and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4

        elif self.blocks[2] == player and self.blocks[5] == player and self.blocks[8] == " ":
            board.update_blocks(8, "O")
            #return 8
        elif self.blocks[5] == player and self.blocks[8] == player and self.blocks[2] == " ":
            board.update_blocks(2, "O")#
            #return 2 
        elif self.blocks[8] == player and self.blocks[2] == player and self.blocks[5] == " ":
            board.update_blocks(5, "O")
            #return 5

        elif self.blocks[0] == player and self.blocks[1] == player and self.blocks[2] == " ":
            board.update_blocks(2, "O")
            #return 2
        elif self.blocks[1] == player and self.blocks[2] == player and self.blocks[0] == " ":
            board.update_blocks(0, "O")
            #return 0
        elif self.blocks[2] == player and self.blocks[0] == player and self.blocks[1] == " ":
            board.update_blocks(1, "O")
            #return 1

        elif self.blocks[3] == player and self.blocks[4] == player and self.blocks[5] == " ":
            board.update_blocks(5, "O")
            #return 5
        elif self.blocks[4] == player and self.blocks[5] == player and self.blocks[3] == " ":
            board.update_blocks(3, "O")
            #return 3
        elif self.blocks[5] == player and self.blocks[3] == player and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4
        
        elif self.blocks[6] == player and self.blocks[7] == player and self.blocks[8] == " ":
            board.update_blocks(8, "O")
            #return 8
        elif self.blocks[7] == player and self.blocks[8] == player and self.blocks[6] == " ":
            board.update_blocks(6, "O")
            #return 6
        elif self.blocks[8] == player and self.blocks[6] == player and self.blocks[7] == " ":
            board.update_blocks(7, "O")
            #return 7

        elif self.blocks[0] == player and self.blocks[4] == player and self.blocks[8] == " ":
            board.update_blocks(8, "O")
            #return 8
        elif self.blocks[4] == player and self.blocks[8] == player and self.blocks[0] == " ":
            board.update_blocks(0, "O")
            #return 0
        elif self.blocks[8] == player and self.blocks[0] == player and self.blocks[4] == " ":
            board.update_blocks(4, "O")
            #return 4
        
        elif self.blocks[2] == player and self.blocks[4] == player and self.blocks[6] == " ":
            board.update_blocks(6, "O")
            #return 6
        elif self.blocks[4] == player and self.blocks[6] == player and self.blocks[2] == " ":
            board.update_blocks(2, "O")
            #return 2 
        elif self.blocks[6] == player and self.blocks[2] == player and self.blocks[4] == " ":
            board.update_blocks(4, "O")
        else :
            self.ai_move("O")

        #choose random
    
    
          
        

board = Board()

def print_header():
    print("\t\t\t WELCOME TO TIC_TAC_TOE\n")

def refresh_screen():
    os.system("clear")
    print_header()
    board.display()

def main(play_again1,choose_leval):
    cnt = 0
    refresh_screen()
    board.reset()
    while True:
        refresh_screen()
        if play_again1 == "Y":
            player1 = player_show("John",board)
            player1.player_move("X")
            if board.winner_player("X"):
                print("\nJohn wins!!\n")
                play_again = raw_input("would you like to play again? (Y/N) >").upper()
                if play_again == "Y":
                    board.reset()
                    cnt = 0
                    continue
            
                else:
                    break
            if board.tie_found():
                print("\nTie Game!!\n")
                play_again = raw_input("would you like to play again? (Y/N) >").upper()
                if play_again == "Y":
                    board.reset()
                    cnt = 0
                    continue
                else:
                    break
            cnt = cnt + 1
            player2 = ai_build("Computer",board)
            if choose_leval == "E":
                player2.ai_move("O")
                refresh_screen()
            elif choose_leval == "H":
                if cnt > 1: 
                    player2.ai_move_sucess("O") 
                    #board.update_blocks(x, "O")
                    refresh_screen()
                    #board.winner_player("O")
                else:
                    player2.ai_move("O")
                    refresh_screen()
            else:
                if cnt > 1: 
                    player2.ai_move_sucess1("O") 
                    #board.update_blocks(x, "O")
                    refresh_screen()
                    #board.winner_player("O")
                else:
                    player2.ai_move("O")
                    refresh_screen()
            if board.winner_player("O"):
                print("\nComputer wins!!\n")
                play_again = raw_input("would you like to play again? (Y/N) >").upper()
                if play_again == "Y":
                    cnt = 0
                    board.reset()
                    continue
                else:
                    break
            if board.tie_found():
                print("\nTie Game!!\n")
                play_again = raw_input("would you like to play again? (Y/N) >").upper()
                if play_again == "Y":
                    cnt = 0
                    board.reset()
                    continue
                else:
                    break
            
        elif play_again1 == "N":
            player1 = player_show("John",board)
            player1.player_move("X")
            if board.winner_player("X"):
                print("\nJohn wins!!\n")
                play_again = raw_input("would you like to play again? (Y/N) >").upper()
                if play_again == "Y":
                    board.reset()
                    cnt = 0
                    continue
            
                else:
                    break
            if board.tie_found():
                print("\nTie Game!!\n")
                play_again = raw_input("would you like to play again? (Y/N) >").upper()
                if play_again == "Y":
                    board.reset()
                    cnt = 0
                    continue
            
                else:
                    break

            player2 = player_show("Joe",board)
            player2.player_move("O")

            # winner
            if board.winner_player("O"):
                print("\nJoe wins!!\n")
                play_again = raw_input("would you like to play again? (Y/N) >").upper()
                if play_again == "Y":
                    cnt = 0
                    board.reset()
                    continue
                else:
                    break
            # tie
            if board.tie_found():
                print("\nTie Game!!\n")
                play_again = raw_input("would you like to play again? (Y/N) >").upper()
                if play_again == "Y":
                    cnt = 0
                    board.reset()
                    continue
                else:
                    break

        elif play_again1 is not ["Y" or "N"]:
            main(play_again1,choose_leval)


if __name__ == "__main__":
   try:
       while True:
           os.system("clear")
           play_again2 = raw_input("would you like to play TIC TAC TOE? (Y/N) >").upper()
           
           if play_again2 == "Y":
               print("If you don't have a friend to play beside computer will play with you")
               play_again1 = raw_input("would you like to play with computer (Y/N) >").upper()
               choose_leval = "H"
               while(True):
                   if play_again1 == "Y":
                       choose_leval = raw_input("Choose leval (E/M/H) >").upper()
                       while(True):
                           if choose_leval in ["H","E","M"]:
                               print("All d best")
                               break
                           elif choose_leval is not ["H","E","M"] :
                               choose_leval = raw_input("Choose leval (E/M/H) >").upper()
                       main(play_again1,choose_leval)
                       break
                   if play_again1 == "N":
                       main(play_again1,choose_leval)
                       break
                   if play_again1 is not ["Y" or "N"]:
                       play_again1 = raw_input("would you like to play with computer (Y/N) >").upper()


           elif play_again2 == "N":
               break
           elif play_again2 is not ["Y" or "N"]:
               os.system("clear")
               play_again1 = raw_input("would you like to play TIC TAC TOE? (Y/N) >").upper()


   except KeyboardInterrupt:
      # do nothing here
      print("\n")
      pass