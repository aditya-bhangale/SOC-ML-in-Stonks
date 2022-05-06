'''
Aditya Bhangale
210070004
'''


board=[[0,1,5,0,0,2,8,0,9],
       [0,0,0,0,0,1,6,0,7],
       [0,7,0,0,0,8,4,0,0],
       [0,0,6,0,1,7,0,4,5],
       [0,5,3,0,0,4,7,0,0],
       [8,4,0,0,9,5,0,6,2],
       [0,0,4,1,7,0,0,8,6],
       [7,6,0,5,2,0,9,1,0],
       [5,9,1,0,8,6,0,0,0]
       ]

#find empty space
def find(bo):
    #print("x")
    for i in range(0,9):
        for j in range(0,9):
            if bo[i][j] == 0:
                return (i,j)  #row, col
    return None

def check_valid(bo,num,row,col):

    for i in range(0,9):
        if(bo[row][i]==num and (col!=i)):
            return False
        if(bo[i][col]==num and (row!=i)):
            return False

    #3*2 grid i.e 3 col 2 row(size x=3 y=2)
    y=row//3
    x=col//3

    for i in range(3*y,3*y+3):
        for j in range(3*x,3*x+3):
             if bo[i][j]==num and (i,j)!=(row,col):
                return False

    return True

def solve(bo):
    f=find(bo)
    #contains row,col if empty found else false(board over)
    if not f:
        return True
    else:
        row,col=f
    #print (row,col)

    for i in range(1,10):
        #numbers 1 to 9
        if(check_valid(bo,i,row,col)):
            bo[row][col]=i

            if(solve(bo)):
                return True
            # recursion to solve other parts
            # if this part comes as false,this i for row,col is wrong and cannot give sudoku soln
            # assign this val to zero again so that some other val of i can be assigned

            bo[row][col]=0

    return False
    #if prog reaches here no soln possible for that values in recursion

def printboard(bo):
    for i in range(0,9):
        for j in range (0,8):
            print (str(bo[i][j])+" ",end="")
        print(bo[i][8])

    print(" ")


printboard(board)
solve(board)
printboard(board)



''' 
 I've referred to online sources for program cuz bahut try karne par nahi aa raha tha ,sorry
learnt the following additional things:any data type can be returned in python function like boolean or numb
                                      :recursion method
'''












