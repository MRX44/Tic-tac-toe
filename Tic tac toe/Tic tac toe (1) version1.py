#tic tac toe game  




class Board():
    
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "] #creat the board


    def display(self):
        #display the board
        
        print(" %s | %s | %s  " %(self.cells[1],self.cells[2],self.cells[3]))
        print("---------")
        print(" %s | %s | %s  " %(self.cells[4],self.cells[5],self.cells[6]))
        print("---------")
        print(" %s | %s | %s  " %(self.cells[7],self.cells[8],self.cells[9]))
        print("  \n")


    def print_header(self):
        print("Welcome to Tic tac toe\n")



    def refresh_screen(self):
        
        self.print_header() #prints the header
        self.display()      #displays the board


class Engine(Board):
    
    def __init__(self):
        Board.__init__(self)
        self.cells = [" "," "," "," "," "," "," "," "," "," "]


    #update the cell 
    def update(self,cell_number,player):
        
        #checks if cell is not taken
        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player
            
        else:
            print("Cell is choosen , please choose another cell! \n")
            if player == "X":
                self.get_x_choice()
            elif player == "O":
                self.get_o_choice()
                
                
        
    #get x choice
    def get_x_choice(self,player= "X"):
        print("X player turn\n")
        self.cell_num = int(input("please enter cell number from 1 to 9  /n"))
        print(" \n")
        


        #checks the cell number is between 1 and 9
        index = True
        while index:
            if self.cell_num >=1 and self.cell_num <=9:
                index = False
            else:
                print("please enter number between 1 and 9\n")
                self.cell_num = int(input("please enter cell number from 1 to 9  /n")) 

                
        self.update(self.cell_num,player)
        self.display()
        




    #get o choice
    def get_o_choice(self,player= "O"):
        print("O player turn\n")
        self.cell_num= int(input("please enter cell number from 1 to 9  /n"))
        print(" \n")
        


        #checks the cell number is between 1 and 9 
        index = True
        while index:
            if self.cell_num >=1 and self.cell_num <=9:
                index = False
            else:
                print("please enter number between 1 and 9\n")
                self.cell_num = int(input("please enter cell number from 1 to 9  \n"))

                
        self.update(self.cell_num,player)
        self.display()


    def is_winner(self):
        #check row 
        if self.cells[1] == self.cells[2] == self.cells[3] and self.cells[1] != " " :
            print("{} wins/n".format(self.cells[1]))
            return True 
        elif self.cells[4] == self.cells[5] == self.cells[6] and self.cells[4] != " " :
            print("{} wins/n".format(self.cells[4]))
            return True 
        elif self.cells[7] == self.cells[8] == self.cells[9] and self.cells[7] != " " :
            print("{} wins/n".format(self.cells[9]))
            return True
        
        #check column
        elif self.cells[1] == self.cells[4] == self.cells[7] and self.cells[4] != " ":
            print("{} wins/n".format(self.cells[1]))
            return True
        elif self.cells[2] == self.cells[5] == self.cells[8] and self.cells[5] != " " :
            print("{} wins/n".format(self.cells[5]))
            return True
        elif self.cells[3] == self.cells[6] == self.cells[9] and self.cells[9] != " " :
            print("{} wins/n".format(self.cells[6]))
            return True 

        #check diagonal
        elif self.cells[1] == self.cells[5] == self.cells[9] and self.cells[1] != " " :
            print("{} wins/n".format(self.cells[1]))
            return True
        elif self.cells[3] == self.cells[5] == self.cells[7] and self.cells[3] != " " :
            print("{} wins/n".format(self.cells[7]))
            return True
        
        return False


    #checks draw game
    def is_draw(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells +=1

        if used_cells == 9:
            print("Draw! /n")
            return True
        else:
            return False


    # resets the game if user wnat to play again
    def reset(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "] 
        
            



board = Engine()
board.refresh_screen()


checker = True

while checker:
    for i in range(1,10):
        if i in [1,3,5,7,9]:
            board.get_x_choice()

        elif i in [2,4,6,8]:
            board.get_o_choice()

            
        if board.is_winner():
            break
        elif board.is_draw():
            break


        
    x= input("Do you want to play again? enter y or n !  ")
    x = x.upper()
    if x == "Y":
        board.reset()
        continue
    elif x == "N":
        checker = False
    else :
        break
        
        

        
            
            
    






