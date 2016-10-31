import cardsBasic


'''
Created on Oct 29, 2016

@author: mary
'''

def setup():
    """
    paramaters: None
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 10 lists, the dealt cards)
    """
    foundation =  [[],[],[],[]]
    tableau =  [[],[],[],[],[],[],[],[],[],[]]
    cell =  [[],[],[],[]]
    
    my_deck = cardsBasic.Deck()
    my_deck.shuffle()
    column = 0    
    
    while not my_deck.is_empty():
        a_card = my_deck.deal()
        cnt= column+1      
        if cnt % 10 == 0:            
            tableau[column].append(a_card) 
            column=0
        else:
            tableau[column].append(a_card)
            column+=1           
    
    
    return foundation,tableau,cell


def move_to_foundation(tableau,foundation,t_col,f_col):
    '''
    parameters: a tableau, a foundation, column of tableau, column of foundation
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    
    
    card_list_in_tableau=tableau[t_col-1]
    if len(card_list_in_tableau) == 0:
        return False
    
    last_card_list_in_tableau=card_list_in_tableau[len(card_list_in_tableau)-1]
    card_list_in_foundation=foundation[f_col-1]
    if len(card_list_in_foundation)==0:
        if last_card_list_in_tableau.get_rank()==1:
                foundation[f_col-1].append(card_list_in_tableau.pop())
        else:
            return False
                
    else:
        last_card_in_foundation=card_list_in_foundation[len(card_list_in_foundation)-1]
        if last_card_list_in_tableau.equal_suit(last_card_in_foundation):
            if last_card_list_in_tableau.get_rank()-1==last_card_in_foundation.get_rank():
                foundation[f_col-1].append(card_list_in_tableau.pop())
            else:
                return False            
        else:
            return False
        
    
    return True
    


def move_to_cell(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    card_list_in_tableau=tableau[t_col-1]  
    if len(card_list_in_tableau) == 0:
            return False
    
    if len(cell[c_col-1])==0:             
        cell[c_col-1].append(card_list_in_tableau.pop())
    else:
        return False;
    
    return True

def move_to_tableau(cell,tableau,c_col,t_col):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    '''
    if len(cell[c_col-1])==0:
        return False;
    else:
        card_list_in_cell=cell[c_col-1]
        card_in_cell = card_list_in_cell[len(card_list_in_cell)-1]
        card_list_in_tableau=tableau[t_col-1]
        if len(card_list_in_tableau)==0:
            if card_in_cell.get_rank()==13:
                card_list_in_tableau.append(cell[c_col-1].pop())
            else:
                return False
        else:
            last_card_in_card_list_in_tableau=card_list_in_tableau[len(card_list_in_tableau)-1]
            if last_card_in_card_list_in_tableau.equal_suit(card_in_cell) and last_card_in_card_list_in_tableau.get_rank() == card_in_cell.get_rank()+1:
                card_list_in_tableau.append(cell[c_col-1].pop())
            else:
                return False
    
    return True;               
         
        

def is_winner(foundation):
    '''
    parameters: a foundation
    return: Boolean
    '''
    if len(foundation[0])==13 and len(foundation[1])==13 and len(foundation[2])==13 and len(foundation[3])==13:
        return True                                                                             
    else:
        return False

def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    card_list_in_tableau_src=tableau[t_col_source-1]
    
    if len(card_list_in_tableau_src)==0:
        return False
    
    card_list_in_tableau_dest=tableau[t_col_dest-1]
    if(len(card_list_in_tableau_src)>0 and len(card_list_in_tableau_dest)>0):
        list_card_in_card_list_in_tableau_src=card_list_in_tableau_src[len(card_list_in_tableau_src)-1]
        list_card_in_card_list_in_tableau_dest = card_list_in_tableau_dest[len(card_list_in_tableau_dest)-1]
        if list_card_in_card_list_in_tableau_src.equal_suit(list_card_in_card_list_in_tableau_dest) and list_card_in_card_list_in_tableau_src.get_rank()+1==list_card_in_card_list_in_tableau_dest.get_rank():
            card_list_in_tableau_dest.append(card_list_in_tableau_src.pop())
        else:
            return False
    elif len(card_list_in_tableau_src)>0 and len(card_list_in_tableau_dest)==0:
        list_card_in_card_list_in_tableau_src=card_list_in_tableau_src[len(card_list_in_tableau_src)-1]
        if list_card_in_card_list_in_tableau_src.get_rank()==13: #K
            card_list_in_tableau_dest.append(card_list_in_tableau_src.pop())
        else:
            return False           
        
    else:
        return False
    
    
    return True
        
def print_game(foundation, tableau,cell):
    """
    parameters: a tableau, a foundation and a cell
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  
        b) print foundation ( can print the top card only)
        c) print cells

    """
    cell_found = '''
      F1      F2      C1      C2      C3      C4      F3      F4
'''
    print(cell_found)

    row = ''
    for stack in foundation[0:2]:
        try:
            row += '%8s' % stack[-1]
        except IndexError:
            row += '%8s' % ''
            
    for c in cell:
        
        try:
            row += '%8s' % c[0]
        except IndexError:
            row += '%8s' % ''
            
    row = row+ ' '
    for stack in foundation[2:]:
        try:
            row += '%8s' % stack[-1]
        except IndexError:
            row += '%8s' % ''

    print (row)
    print ('----------')


    
    print ("Tableau")
    row = ''
    for i in range(len(tableau)):
        row += '%8s' % (i + 1)
    print (row)

    """find the length of the longest stack"""
    stack_length = []
    for stack in tableau:
        stack_length.append(len(stack))
    max_length = max(stack_length)

    for i in range(max_length):
        row = ''                    # remember to clear the row
        for stack in tableau:
            try:
                row += '%8s' % stack[i]
            except IndexError:
                row += '%8s' % ''
        print (row)
    print ('----------')

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    to_print ='''Rules of Seahaven Towers

    a. Only one card at a time can be moved.
    b. Foundation
        Each foundation holds only one suit and is built up from Ace to King.
        You can move a card to the foundation from a cell or the tableau.
        Once a card is on the foundation it cannot be moved off.
    c. Tableau 
        i. The card at the bottom of a column may be moved to an open cell,
           a foundation or another column of the tableau.
        ii. Moving a card to a tableau column follows these rules
            1. A card can only be moved to the bottom of a column
            2. When you move a card to a column in the tableau you can only
               build down by rank and by the same color. For example, you
               can move a Two of Hearts onto a Three of Hearts (the pile goes
               down by rank, and same color)
        iii. Empty columns may be filled only by a King with any color.
    d. Cell
        i. One cell spot can only contain 1 card
        ii. The card may be moved to the tableau or the foundation.
'''
    print(to_print)

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    response ='''
    Responses are:
    --------------
         t2f T F   - move from Tableau T to Foundation F (T and F are ints)
	 t2c T C   - move from Tableau T to Cell C (T and C are ints)
	 t2t T1 T2 - move from Tableau T1 to Tableau T2 (T1 and T2 are ints)
	 c2t C T   - move from Cell C to Tableau T (C and T are ints)
	 c2f C F   - move from Cell C to Foundation F (C and F are ints)
	 'h' for help
	 'q' to quit
         '''
    print (response)
         

def check_input_param(input_list):
    try:
        if len(input_list)==1 and input_list[0]=='h' or input_list[0]=='q':
            return True
        
        index1 = int(input_list[1])
        index2 = int(input_list[2])
        if len(input_list)!=3 or not isinstance(index1, int) or not isinstance(index2, int) or index1==0 or index2==0:
            return False    
    except:     
        return False
    
    return True  
def play():
    ''' 
    main program. Does error checking on the user input. 
    '''
    print_rules()
    foundation, tableau, cell = setup()     
       
    show_help()
    while True:
        # Uncomment this next line. It is commented out because setup doesn't do anything so printing doesn't work.
        print_game(foundation, tableau, cell)
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split() 
        if not check_input_param(response_list):
            print("Invalid input, please try again ")            
        elif len(response_list) > 0:
            r = response_list[0]
            if r == 't2f':
                if not move_to_foundation(tableau, foundation, int(response_list[1]), int(response_list[2])):
                    print("Invalid move.") 
                elif is_winner(foundation):
                    print("Congrats: you win!")
                    break                       
            elif r == 't2t':
                if not move_in_tableau(tableau, int(response_list[1]), int(response_list[2])):
                    print("Invalid move.") 
                elif is_winner(foundation):
                    print("Congrats: you win!")
                    break                     
            elif r == 't2c':
                if not move_to_cell(tableau, cell, int(response_list[1]), int(response_list[2])):
                    print("Invalid move.") 
                elif is_winner(foundation):
                    print("Congrats: you win!")
                    break                          
            elif r == 'c2t':
                if not move_to_tableau(cell, tableau, int(response_list[1]), int(response_list[2])):
                    print("Invalid move.") 
                elif is_winner(foundation):
                    print("Congrats: you win!")
                    break                          
            elif r == 'c2f':
                if not move_to_foundation(cell, foundation, int(response_list[1]), int(response_list[2])):
                    print("Invalid move.")  
                elif is_winner(foundation):
                    print("Congrats: you win!")
                    break                    
            elif r == 'q':
                break
            elif r == 'h':
                show_help()
            else:
                print('Unknown command:',r)
        else:
            print("Unknown Command:",response)
    print('Thanks for playing')

play()


        
    

