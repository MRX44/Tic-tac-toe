import pygame 

 
pygame.init() #initiate pygame 
win = pygame.display.set_mode((800,550)) #set the window 
pygame.display.set_caption("Tic tac toe") # set title
win.fill((255,255,255)) #set backgroud

start_button =  pygame.draw.rect(win,(250,200,100),(550,30,200,150))
result_board  =  pygame.draw.rect(win,(250,200,100),(550,200,200,150))
score_board =  pygame.draw.rect(win,(250,200,100),(550,370,200,150))



font = pygame.font.SysFont(None, 80)
start = font.render('Start', True, (0,0,255))
win.blit(start, (580,80))









#Create buttons
x = 30  #x position
y = 30  #Y position
h = 150 #height
w = 150 #wedith

#a variable to store in the value of the buttons
board = [[0,1,2],[3,4,5],[6,7,8]]


lst=[] #a list contains all buttons
for i in range(3): 
    for j in range(3):
        lst.append(pygame.draw.rect(win,(0,0,0),((x+(w*j)+(20*j)),(y+(h*i)+(20*i)),w,h)))
    



def draw_x(x,y):
    #this function draws X shape
    
    pygame.draw.line(win,(255,0,0),(x,y),(x+100,y+100),15)
    pygame.draw.line(win,(255,0,0),(x+100,y),(x,y+100),15)
    

def draw_o(x,y):
    #this function draws O shape
    pygame.draw.circle(win,(0,255,0),(x,y),50)

    
def reset():
    lst=[]
    for i in range(3): 
        for j in range(3):
            lst.append(pygame.draw.rect(win,(0,0,0),((x+(w*j)+(20*j)),(y+(h*i)+(20*i)),w,h)))




def is_winner(p):
    if board[0][0]== board[0][1] == board[0][2] == p or board[1][0]== board[1][1] == board[1][2] ==p or \
       board[2][0]== board[2][1] == board[2][2] == p or board[0][0]== board[1][0] == board[2][0] ==p or \
       board[1][1]== board[0][1] == board[2][1] == p or board[2][2]== board[1][2] == board[0][2] ==p or \
       board[0][0]== board[1][1] == board[2][2] == p or board[0][2]== board[1][1] == board[2][0] ==p:
        print("{} player wins".format(p))
        return True
    else : return False 
            
  
first_choice = True
lst_of_choices = [True for i in range(9)] # list of choices for every cell
draw_object = "circle"



run = True
while run:
    pygame.time.delay(10)
    
    for event in pygame.event.get():           #checks the events and get them   

        
        if event.type == pygame.QUIT:          #checks the exit button 
            run = False

        if event.type == pygame.KEYDOWN:        #checks the space button
            if event.key == pygame.K_SPACE:     #space button used to reset the screen
                reset()
                lst_of_choices = [True for i in range(9)]
                result_board  =  pygame.draw.rect(win,(250,200,100),(550,200,200,150))
                used_cells = 0
               
                


        if event.type == pygame.MOUSEBUTTONUP: #checks the mouse click
            pos = pygame.mouse.get_pos()       #gets the position of the click of the  mouse 
            #print(pos)
            
            if start_button.collidepoint(pos):
                
                s = True
                used_cells=0
                x_scoore = 0
                o_scoore = 0
                
                
            
            try:    
                if s:
                    print(x_scoore)
                    #
                    #
                    
                    # asks if the click inside first button
                    if lst[0].collidepoint(pos) and lst_of_choices[0]:
                        used_cells += 1
                        if draw_object == "circle"  :
                            draw_o(100,100)
                            draw_object = "line"
                            board[0][0] = "o"
                        else :
                            draw_x(50,50)
                            draw_object = "circle"
                            board[0][0] = "x"
                        lst_of_choices[0]  = False
                       
                        
                    if lst[1].collidepoint(pos) and lst_of_choices[1] :
                        used_cells += 1
                        if draw_object == "circle":
                            draw_o(270,100)
                            draw_object = "line"
                            board[0][1] = "o"
                        else:
                            draw_x(220,50)
                            draw_object = "circle"
                            board[0][1] = "x"
                        lst_of_choices[1] = False

                    


                    if lst[2].collidepoint(pos) and lst_of_choices[2]:
                        used_cells += 1
                        if draw_object == "circle":
                            draw_o(440,100)
                            draw_object = "line"
                            board[0][2] = "o"
                        else:
                            draw_x(390,50)
                            draw_object = "circle"
                            board[0][2] = "x"
                        lst_of_choices[2] = False



                    if lst[3].collidepoint(pos) and lst_of_choices[3]:
                        used_cells += 1
                        if draw_object == "circle":
                            draw_o(100,270)
                            draw_object = "line"
                            board[1][0] = "o"
                        else:
                            draw_x(50,220)
                            draw_object = "circle"
                            board[1][0] = "x"
                        lst_of_choices[3]= False



                    if lst[4].collidepoint(pos) and lst_of_choices[4] :
                        used_cells += 1
                        if draw_object == "circle":
                            draw_o(270,270)
                            draw_object = "line"
                            board[1][1] = "o"
                        else:
                            draw_x(220,220)
                            draw_object = "circle"
                            board[1][1] = "x"                
                        lst_of_choices[4]= False
                        

                    if lst[5].collidepoint(pos) and lst_of_choices[5]:
                        used_cells += 1
                        if draw_object == "circle":
                            draw_o(440,270)
                            draw_object = "line"
                            board[1][2] = "o"
                        else:
                            draw_x(390,220)
                            draw_object = "circle"
                            board[1][2] = "x"
                        lst_of_choices[5] = False
                        

                    if lst[6].collidepoint(pos) and lst_of_choices[6] :
                        used_cells += 1
                        if draw_object == "circle":
                            draw_o(100,440)
                            draw_object = "line"
                            board[2][0] = "o"
                        else:
                            draw_x(50,390)
                            draw_object = "circle"
                            board[2][0] = "x"
                        lst_of_choices[6] = False
                        

                    if lst[7].collidepoint(pos) and lst_of_choices[7] :
                        used_cells += 1
                        if draw_object == "circle":
                            draw_o(270,440)
                            draw_object = "line"
                            board[2][1] = "o"
                        else:
                            draw_x(220,390)
                            draw_object = "circle"
                            board[2][1] = "x"
                        lst_of_choices[7] = False
                        

                    if lst[8].collidepoint(pos) and lst_of_choices[8] :
                        used_cells += 1
                        if draw_object == "circle":
                            draw_o(440,440)
                            draw_object = "line"
                            board[2][2] = "o"
                        else:
                            draw_x(390,390)
                            draw_object = "circle"
                            board[2][2] = "x"
                        lst_of_choices[8] = False
                    
                    
                    if is_winner("x"):
                        x_scoore +=1
                        score_board =  pygame.draw.rect(win,(250,200,100),(550,370,200,150))
                        board = [[0,1,2],[3,4,5],[6,7,8]]
                        show_X="X wins"
                        result_x = font.render(show_X, True, (0,0,255))
                        win.blit(result_x, (560,250))
                        
                        lst_of_choices = [False for i in range(9)]

                        
                    elif is_winner("o"):
                        o_scoore +=1
                        score_board =  pygame.draw.rect(win,(250,200,100),(550,370,200,150))
                        board = [[0,1,2],[3,4,5],[6,7,8]]
                        show="O wins"
                        result = font.render(show, True, (0,0,255))
                        win.blit(result, (560,250))
                        lst_of_choices = [False for i in range(9)]



                    elif used_cells == 9 :
                        draw = font.render("Draw", True, (0,0,255))
                        win.blit(draw, (560,250))
                        board = [[0,1,2],[3,4,5],[6,7,8]]
                        used_cells = 0
                        
                    xstring= str(x_scoore) + "for x"
                    ostring = str(o_scoore) + "for o"

                    
                    scored = font.render(xstring, True, (0,0,255))
                    win.blit(scored, (580,380))
                    scored2 = font.render(ostring, True, (0,0,255))
                    win.blit(scored2, (580,440))
                   



                        
                else:
                    continue

                
            except NameError:
                pass

               

    
    pygame.display.update() #update the surface

pygame.quit() 
