from tkinter import *
from tkinter import ttk
CheckList = [[" "," "," "],[" "," "," "],[" "," "," "]]
CheckDic = {1:[0,0,1],2:[0,1],3:[0,2,2],4:[1,0],5:[1,1,1,2],6:[1,2],7:[2,0,2],8:[2,1],9:[2,2,1]}

def Victory(Symb,Pos):

    row = CheckDic[Pos][0]
    col = CheckDic[Pos][1]
    flag = 1
    for i in range(0,3):
        print("I",i)
        if CheckList[row][i] !=Symb:
            flag = 0
            break
    #print("I",i)
    if flag == 1:
        print("Returning i")
        return 1
    flag = 1
    for j in range(0,3):
        print("j",j)
        if CheckList[j][col] != Symb:
            flag = 0
            break
    #print("J",j)
    if flag == 1:
        print("Returning j")
        return 1

    if(len(CheckDic[Pos]) == 3):
        if(CheckDic[Pos][2] == 1):
            ctr = 0
            for k in range(0,3):
                for m in range(0,3):
                    if k == m:
                        if(CheckList[k][m] == Symb):
                            ctr += 1
            if(ctr == 3):
                return 1

        elif(CheckDic[Pos][2] == 2):
            ctr = 0
            for k in range(0,3):
                for m in range(0,3):
                    if k + m == 2:
                        if CheckList[k][m] == Symb:
                            ctr += 1
            if(ctr == 3):
                return 1

    elif(len(CheckDic[Pos]) == 4):
        if (CheckDic[Pos][2] == 1):
            ctr = 0
            for k in range(0, 3):
                for m in range(0, 3):
                    if k == m:
                        if (CheckList[k][m] == Symb):
                            ctr += 1
            if (ctr == 3):
                return 1

        elif (CheckDic[Pos][2] == 2):
            ctr = 0
            for k in range(0, 3):
                for m in range(0, 3):
                    if k + m == 2:
                        if CheckList[k][m] == Symb:
                            ctr += 1
            if (ctr == 3):
                return 1

        if (CheckDic[Pos][3] == 1):
            ctr = 0
            for k in range(0, 3):
                for m in range(0, 3):
                    if k == m:
                        if (CheckList[k][m] == Symb):
                            ctr += 1
            if (ctr == 3):
                return 1

        elif (CheckDic[Pos][3] == 2):
            ctr = 0
            for k in range(0, 3):
                for m in range(0, 3):
                    if k + m == 2:
                        if CheckList[k][m] == Symb:
                            ctr += 1
            if (ctr == 3):
                return 1

    count = 0
    for l in range(0,3):
        if " " not in CheckList[l]:
            count += 1
            print("Count",count)
    if count == 3:
        Turn.set("Game Draw")











    '''
    for i in range(0,len(CheckDic[Pos])):
        if (ctr == 3 and Symb == "X"):
            print("Won")
            Turn.set("Player A Won")
            break
        elif (ctr == 3 and Symb == "O"):
            print("Won")
            Turn.set("Player B Won")
            break

        if i ==0:
            for j in range(0,3):
                if(CheckList[CheckDic[Pos][i]][j] == Symb):
                    ctr+=1
            print(ctr)
        elif i == 1:
            for k in range(0,3):
                if(CheckList[k][CheckDic[Pos][i]] == Symb):
                    ctr+=1
            print(ctr)
        elif i == 2:
            if(CheckDic[Pos][i] == 1):
                for k in range(0,3):
                    for m in range(0,3):
                        if(k==m):
                            if(CheckList[k][m] == Symb):
                                ctr+=1
                print(ctr)
    '''





def Reset():
    global CheckList
    Symbol1.set(" ")
    Symbol2.set(" ")
    Symbol3.set(" ")
    Symbol4.set(" ")
    Symbol5.set(" ")
    Symbol6.set(" ")
    Symbol7.set(" ")
    Symbol8.set(" ")
    Symbol9.set(" ")
    Turn.set("Player A's Turn")
    Button1.config(fg="black")
    Button2.config(fg="black")
    Button3.config(fg="black")
    Button4.config(fg="black")
    Button5.config(fg="black")
    Button6.config(fg="black")
    Button7.config(fg="black")
    Button8.config(fg="black")
    Button9.config(fg="black")
    CheckList = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def FillBox1():
    CurrentTurn = Turn.get()
    CurrentSymbol = (Symbol1.get())
    if(Turn.get() == "Player A's Turn" and Symbol1.get() == " "):
        Symbol1.set("X")
        Button1.config(fg="red")
        CheckList[0][0] = "X"
        print(Symbol1.get())
        Turn.set("Player B's Turn")
        print(Turn.get())
        Check = Victory(Symbol1.get(), 1)
        if Check == 1:
            Turn.set("Player A Won")


    elif(Turn.get() == "Player B's Turn" and Symbol1.get() == " "):
        Symbol1.set("O")
        Button1.config(fg="green")
        CheckList[0][0] = "O"
        Turn.set("Player A's Turn")
        Check = Victory(Symbol1.get(), 1)
        if Check == 1:
            Turn.set("Player B Won")

    print(CheckList)
def FillBox2():
        CurrentTurn = Turn.get()
        CurrentSymbol = (Symbol1.get())
        if (Turn.get() == "Player B's Turn" and Symbol2.get() == " "):
            Symbol2.set("O")
            Button2.config(fg="green")
            CheckList[0][1] = "O"
            print(Symbol1.get())
            Turn.set("Player A's Turn")
            print(Turn.get())
            Check = Victory(Symbol2.get(), 2)
            if Check == 1:
                Turn.set("Player B Won")

        elif(Turn.get() == "Player A's Turn" and Symbol2.get() == " "):
            Symbol2.set("X")
            Button2.config(fg="red")
            CheckList[0][1] = "X"
            #Victory(Symbol2.get(),2)
            Turn.set("Player B's Turn")
            Check = Victory(Symbol2.get(), 2)
            if Check == 1:
                Turn.set("Player A Won")
        print(CheckList)

def FillBox3():
    CurrentTurn = Turn.get()
    CurrentSymbol = (Symbol1.get())
    if (Turn.get() == "Player B's Turn" and Symbol3.get() == " "):
        Symbol3.set("O")
        Button3.config(fg="green")
        CheckList[0][2] = "O"
        print(Symbol1.get())
        Turn.set("Player A's Turn")
        print(Turn.get())
        Check = Victory(Symbol3.get(), 3)
        if Check == 1:
            Turn.set("Player B Won")

    elif (Turn.get() == "Player A's Turn" and Symbol3.get() == " "):
        Symbol3.set("X")
        Button3.config(fg="red")
        CheckList[0][2] = "X"
        #Victory(Symbol3.get(),3)
        Turn.set("Player B's Turn")
        Check = Victory(Symbol3.get(), 3)
        if Check == 1:
            Turn.set("Player A Won")
    print(CheckList)

def FillBox4():
    CurrentTurn = Turn.get()
    CurrentSymbol = (Symbol1.get())
    if (Turn.get() == "Player B's Turn" and Symbol4.get() == " "):
        Symbol4.set("O")
        Button4.config(fg="green")
        CheckList[1][0] = "O"
        print(Symbol1.get())
        Turn.set("Player A's Turn")
        print(Turn.get())
        Check = Victory(Symbol4.get(), 4)
        if Check == 1:
            Turn.set("Player B Won")

    elif (Turn.get() == "Player A's Turn" and Symbol4.get() == " "):
        Symbol4.set("X")
        Button4.config(fg="red")
        CheckList[1][0] = "X"
        Turn.set("Player B's Turn")
        Check = Victory(Symbol4.get(), 4)
        if Check == 1:
            Turn.set("Player A Won")
    print(CheckList)

def FillBox5():
    CurrentTurn = Turn.get()
    CurrentSymbol = (Symbol1.get())
    if (Turn.get() == "Player B's Turn" and Symbol5.get() == " "):
        Symbol5.set("O")
        Button5.config(fg="green")
        CheckList[1][1] = "O"
        print(Symbol1.get())
        Turn.set("Player A's Turn")
        print(Turn.get())
        Check = Victory(Symbol5.get(), 5)
        if Check == 1:
            Turn.set("Player B Won")

    elif (Turn.get() == "Player A's Turn" and Symbol5.get() == " "):
        Symbol5.set("X")
        Button5.config(fg="red")
        CheckList[1][1] = "X"
        Turn.set("Player B's Turn")
        Check = Victory(Symbol5.get(), 5)
        if Check == 1:
            Turn.set("Player A Won")
    print(CheckList)

def FillBox6():
    CurrentTurn = Turn.get()
    CurrentSymbol = (Symbol1.get())
    if (Turn.get() == "Player B's Turn" and Symbol6.get() == " "):
        Symbol6.set("O")
        Button6.config(fg="green")
        CheckList[1][2] = "O"
        print(Symbol1.get())
        Turn.set("Player A's Turn")
        print(Turn.get())
        Check = Victory(Symbol6.get(), 6)
        if Check == 1:
            Turn.set("Player B Won")

    elif (Turn.get() == "Player A's Turn" and Symbol6.get() == " "):
        Symbol6.set("X")
        Button6.config(fg="red")
        CheckList[1][2] = "X"
        Turn.set("Player B's Turn")
        Check = Victory(Symbol6.get(), 6)
        if Check == 1:
            Turn.set("Player A Won")
    print(CheckList)



def FillBox7():
    CurrentTurn = Turn.get()
    CurrentSymbol = (Symbol1.get())
    if (Turn.get() == "Player B's Turn" and Symbol7.get() == " "):
        Symbol7.set("O")
        Button7.config(fg="green")
        CheckList[2][0] = "O"
        print(Symbol1.get())
        Turn.set("Player A's Turn")
        print(Turn.get())
        Check = Victory(Symbol7.get(), 7)
        if Check == 1:
            Turn.set("Player B Won")

    elif (Turn.get() == "Player A's Turn" and Symbol7.get() == " "):
        Symbol7.set("X")
        Button7.config(fg="red")
        CheckList[2][0] = "X"
        Turn.set("Player B's Turn")
        Check = Victory(Symbol7.get(), 7)
        if Check == 1:
            Turn.set("Player A Won")
    print(CheckList)

def FillBox8():
    CurrentTurn = Turn.get()
    CurrentSymbol = (Symbol1.get())
    if (Turn.get() == "Player B's Turn" and Symbol8.get() == " "):
        Symbol8.set("O")
        Button8.config(fg="green")
        CheckList[2][1] = "O"
        print(Symbol1.get())
        Turn.set("Player A's Turn")
        print(Turn.get())
        Check = Victory(Symbol8.get(), 8)
        if Check == 1:
            Turn.set("Player B Won")

    elif (Turn.get() == "Player A's Turn" and Symbol8.get() == " "):
        Symbol8.set("X")
        Button8.config(fg="red")
        CheckList[2][1] = "X"
        Turn.set("Player B's Turn")
        Check = Victory(Symbol8.get(), 8)
        if Check == 1:
            Turn.set("Player A Won")
    print(CheckList)

def FillBox9():
    CurrentTurn = Turn.get()
    CurrentSymbol = (Symbol1.get())
    if (Turn.get() == "Player B's Turn" and Symbol9.get() == " "):
        Symbol9.set("O")
        Button9.config(fg="green")
        CheckList[2][2] = "O"
        print(Symbol1.get())
        Turn.set("Player A's Turn")
        print(Turn.get())
        Check = Victory(Symbol9.get(), 9)
        if Check == 1:
            Turn.set("Player B Won")

    elif (Turn.get() == "Player A's Turn" and Symbol9.get() == " "):
        Symbol9.set("X")
        Button9.config(fg="red")
        CheckList[2][2] = "X"
        Turn.set("Player B's Turn")
        Check = Victory(Symbol9.get(), 9)
        if Check == 1:
            Turn.set("Player A Won")
    print(CheckList)

MainBgColor = "#3c91e6"
MainWindow = Tk()
MainWindow.geometry("500x500")
MainWindow.config(bg = MainBgColor)
HeadFrame = Frame(MainWindow,bg=MainBgColor,padx = 100,pady = 10)
HeadFrame.grid(row = 0)

GameHeading = Label(HeadFrame,bg ="#5b5c5d",fg = "white",text="Welcome To XO World",font="Arial 24")
GameHeading.pack()

TurnFrame = Frame(MainWindow,bg=MainBgColor,padx= 120,pady = 10)
TurnFrame.grid(row = 1)
Turn = StringVar()
Turn.set("Player A's Turn")
TurnHeading = Label(TurnFrame,bg = "#d9dcde",fg="black",textvariable=Turn,font="Arial 18")
TurnHeading.pack()

ButtonFrame1 = Frame(MainWindow,bg=MainBgColor,padx = 80,pady=10)
ButtonFrame1.grid(row = 3)

Symbol1= StringVar()
Symbol1.set(" ")

Symbol2= StringVar()
Symbol2.set(" ")

Symbol3= StringVar()
Symbol3.set(" ")

Button1 = Button(ButtonFrame1,textvariable=Symbol1,command=FillBox1,width=4,height=2)
Button1.grid(row = 3 ,column = 0,padx=10)
Button2 = Button(ButtonFrame1,textvariable=Symbol2,command = FillBox2,width=4,height=2)
Button2.grid(row = 3 ,column = 1,padx=10)
Button3 = Button(ButtonFrame1,textvariable=Symbol3,command = FillBox3,width=4,height=2)
Button3.grid(row = 3 ,column = 2,padx=10)



ButtonFrame2 = Frame(MainWindow,bg = MainBgColor,padx = 80,pady=10)
ButtonFrame2.grid(row = 4)

Symbol4= StringVar()
Symbol4.set(" ")
Symbol5= StringVar()
Symbol5.set(" ")
Symbol6= StringVar()
Symbol6.set(" ")

Button4 = Button(ButtonFrame2,textvariable=Symbol4,command=FillBox4,width=4,height=2)
Button4.grid(row = 3 ,column = 0,padx=10)
Button5 = Button(ButtonFrame2,textvariable=Symbol5,command = FillBox5,width=4,height=2)
Button5.grid(row = 3 ,column = 1,padx=10)
Button6 = Button(ButtonFrame2,textvariable=Symbol6,command = FillBox6,width=4,height=2)
Button6.grid(row = 3 ,column = 2,padx=10)

ButtonFrame3 = Frame(MainWindow,bg=MainBgColor,padx = 80,pady=10)
ButtonFrame3.grid(row = 5)

Symbol7= StringVar()
Symbol7.set(" ")
Symbol8= StringVar()
Symbol8.set(" ")
Symbol9= StringVar()
Symbol9.set(" ")

Button7 = Button(ButtonFrame3,textvariable=Symbol7,command=FillBox7,width=4,height=2)
Button7.grid(row = 3 ,column = 0,padx=10)
Button8 = Button(ButtonFrame3,textvariable=Symbol8,command = FillBox8,width=4,height=2)
Button8.grid(row = 3 ,column = 1,padx=10)
Button9 = Button(ButtonFrame3,textvariable=Symbol9,command = FillBox9,width=4,height=2)
Button9.grid(row = 3 ,column = 2,padx=10)

ButtonFrame4 = Frame(MainWindow,bg=MainBgColor,padx = 80,pady=10)
ButtonFrame4.grid(row = 7)

ResetBut = Button(ButtonFrame4,text="New Game",command = Reset)
ResetBut.grid(row=7,column=1,padx=10)

ExitBut = Button(ButtonFrame4,text = "GIVE UP",command =MainWindow.destroy)
ExitBut.grid(row =7,column=2,padx=10)
MainWindow.mainloop()



