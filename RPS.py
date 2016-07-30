import random

#initialise the variables
umove=''
cmove=''

score = [0,0]

print("Rock(R),Paper(P),Scissors(S)")
moves = ['R','r','P','p','S','s'] #for specifing the moves

#user move
def move():
    global umove
    umove = input("Enter R,P,S").upper()
    if umove in moves: #Retry if illegal move.
        print("Your Move "+umove)
    else:
        move() 

#computer move
def comove():
    global cmove
    cmove = random.randint(1,3)
    if cmove == 1:
        cmove='R'
    elif cmove == 2:
        cmove='P'
    else:
        cmove='S'
    print("Computers Move")
    print(cmove)

def compute():
    global score
    if umove == cmove:
        print("Draw")
    elif umove == 'R':
        if cmove == 'S':
            print("Rock Smashes Sissors,you win")
            score[0] = score[0] + 1
        if cmove == 'P':
            print("Paper Covers Rock,you loose")
            score[1] = score[1] + 1
    elif umove == 'P':
        if cmove == 'S':
            print("Scissors cut paper,you loose")
            score[1] = score[1] + 1
        if cmove == 'R':
            print("Paper Covers Rock,you win")
            score[0] = score[0] + 1
    elif umove == 'S':
        if cmove == 'R':
            print("Rock Smashes Sissors,you loose")
            score[1] = score[1] + 1
        if cmove == 'P':
            print("Scissors cut paper,you win")
            score[0] = score[0] + 1
    
def restart():
    print("The Scores are, You - ",score[0]," Comp Score",score[1])
    res = input("Do you want to restart? Y/N  ").upper()
    if res == 'Y':
       start()
    else:
        print("Final Scores are, You - ",score[0]," Comp Score",score[1])
        print("Exiting")

        
#for restarting the game
def start():
    move()
    comove()
    compute()
    restart()

move()
comove()
compute()
restart()
