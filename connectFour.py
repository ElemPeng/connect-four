from console import clear
"""
The connect four grid is seven squares wide by six squares high.
"B" means black (plays first)
"W" means white (plays second)
" " means empty
"""
class newGame:
    def __init__(self):
        #board[i,j] refers to the ith element of column j. 
        self.board=['      ' for j in range(7)]
        self.turn='B'
        
    def play(self,column):
        if self.board[column][5]!=' ': return False
        else: 
            self.board[column]=self.board[column].strip()+self.turn
            self.board[column]+=' '*(6-len(self.board[column]))
            if self.turn=='B': self.turn='W'
            else: self.turn='B'
            return True
    
    def print(self):
        print("+-"*7+"+")
        for row in range(6)[::-1]:
            for column in range(7):
                print("|", end=self.board[column][row])
            print('|')
        print("+-"*7+"+")
        print(' '+' '.join(str(num) for num in range(1,8))+' ')
    
    def isOver(self):
        wins=["BBBB","WWWW"]
        #horizonal
        for column in range(4):
            for row in range(6):
                if ''.join([self.board[column+i][row] for i in range(4)]) in wins: return self.board[column][row]
                #up,diag
                if row<3:
                   if ''.join([self.board[column+i][row+i] for i in range(4)]) in wins: return self.board[column][row] 
                #dowm diag
                if row>2:
                  if ''.join([self.board[column+i][row-i] for i in range(4)]) in wins: return self.board[column][row] 
        
        #vertical
        for column in self.board:
                for i in range(3):
                    if column[i:i+4] in wins: return column[i]    
        #draw
        if ' ' not in ''.join(self.board):return 'D'
        # keep going
        return 'N'
        
abbrev={'B':"Black",'W':"White"}       
game=newGame()
while game.isOver()=='N':
    clear()
    game.print()
    print(abbrev[game.turn]+"'s turn")
    choice=-1
    while not(0<=choice and choice<=7):
        try:
            choice=int(input("Type in a column from 1 to 7 (0 quits): "))
            assert 0<=choice and choice<=7
            if choice!=0: assert game.play(choice-1)
        except:
            if 1<=choice and choice<=7: print("\nColumn "+str(choice)+" is full!")
            else: print("\nImproper Input!") 
    if choice==0: break  

if choice!=0:
    clear()
    game.print()
    if game.isOver()=='D': print("Draw!")
    else: print(abbrev[game.isOver()]+" wins!")
