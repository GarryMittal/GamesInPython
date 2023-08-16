from tkinter import *
import random

class ST:
    def __init__(self,ShuffleMain):
        self.mainw = ShuffleMain
        self.frame = Frame(self.mainw,bg="red")
        self.frame.grid(row=0)
    def ButtonGrid(self):

        self.MyGrid = []
        for x in range(0,4):
            row = []
            for y in range(0,4):
                row.append(Button(self.frame,text=ShuffleList[x][y],command=lambda i=x,j=y:self.OnClick(i,j),font="Arial 15 ",height=5,width=10,bg="gray"))
                row[-1].grid(row=x,column=y)
            self.MyGrid.append(row)

    def ChangeColor(self):
        for x in range(4):

            for y in range(4):
                self.MyGrid[x][y]['bg'] = "#3c91e6"
                self.MyGrid[x][y]['text'] = str(self.MyGrid[x][y]['text'])+"\U0001F600"
                self.MyGrid[x][y]['state'] = DISABLED
    def OnClick(self,i,j):
        print(ShuffleList[i][j])
        print("I",i)
        print("J",j)
        print(ShuffleList[i])

        if i == 0:
            if j == 0:
                if ShuffleList[0][1] == " ":
                    ShuffleList[0][0],ShuffleList[0][1] = ShuffleList[0][1],ShuffleList[0][0]
                elif ShuffleList[1][0] == " ":
                    ShuffleList[0][0], ShuffleList[1][0] = ShuffleList[1][0], ShuffleList[0][0]
            elif j == 3:
                if ShuffleList[0][2] == " ":
                    ShuffleList[0][3],ShuffleList[0][2] = ShuffleList[0][2],ShuffleList[0][3]
                elif ShuffleList[1][3] == " ":
                    ShuffleList[0][3], ShuffleList[1][3] = ShuffleList[1][3], ShuffleList[0][3]
            else:
                if ShuffleList[0][j-1] == " ":
                    ShuffleList[0][j],ShuffleList[0][j-1] = ShuffleList[0][j-1],ShuffleList[0][j]
                elif ShuffleList[0][j+1] == " ":
                    ShuffleList[0][j],ShuffleList[0][j+1] = ShuffleList[0][j+1],ShuffleList[0][j]
                elif ShuffleList[1][j] == " ":
                    ShuffleList[0][j],ShuffleList[1][j] = ShuffleList[1][j],ShuffleList[0][j]

        elif i == 3:

            if j == 0:
                if ShuffleList[3][1] == " ":
                    ShuffleList[3][0],ShuffleList[3][1] = ShuffleList[3][1],ShuffleList[3][0]
                elif ShuffleList[2][0] == " ":
                    ShuffleList[3][0],ShuffleList[2][0] = ShuffleList[2][0],ShuffleList[3][0]
            elif j == 3:
                if ShuffleList[3][2] == " ":
                    ShuffleList[3][3],ShuffleList[3][2] = ShuffleList[3][2],ShuffleList[3][3]
                elif ShuffleList[2][3] == " ":
                    ShuffleList[3][3],ShuffleList[2][3] = ShuffleList[2][3],ShuffleList[3][3]
            else:
                if ShuffleList[3][j-1] == " ":
                    ShuffleList[3][j],ShuffleList[3][j-1] = ShuffleList[3][j-1],ShuffleList[3][j]
                elif ShuffleList[3][j+1] == " ":
                    ShuffleList[3][j],ShuffleList[3][j+1]= ShuffleList[3][j+1],ShuffleList[3][j]
                elif ShuffleList[2][j] == " ":
                    ShuffleList[3][j],ShuffleList[2][j] = ShuffleList[2][j],ShuffleList[3][j]
        else:
            if j == 0:
                if ShuffleList[i][1] == " ":
                    ShuffleList[i][0],ShuffleList[i][1] = ShuffleList[i][1],ShuffleList[i][0]
                elif ShuffleList[i-1][0] == " ":
                    ShuffleList[i][0],ShuffleList[i-1][0] = ShuffleList[i-1][0],ShuffleList[i][0]
                elif ShuffleList[i+1][0] == " ":
                    ShuffleList[i][0],ShuffleList[i+1][0] = ShuffleList[i+1][0],ShuffleList[i][0]
            elif j == 3:
                if ShuffleList[i][2] == " ":
                    ShuffleList[i][3],ShuffleList[i][2] = ShuffleList[i][2],ShuffleList[i][3]
                elif ShuffleList[i-1][3] == " ":
                    ShuffleList[i][3],ShuffleList[i-1][3] = ShuffleList[i-1][3],ShuffleList[i][3]
                elif ShuffleList[i+1][3] == " ":
                    ShuffleList[i][3],ShuffleList[i+1][3] = ShuffleList[i+1][3],ShuffleList[i][3]
            else:
                if ShuffleList[i][j+1] == " ":
                    ShuffleList[i][j],ShuffleList[i][j+1] = ShuffleList[i][j+1],ShuffleList[i][j]
                elif ShuffleList[i][j-1] == " ":
                    ShuffleList[i][j],ShuffleList[i][j-1] = ShuffleList[i][j-1],ShuffleList[i][j]
                elif ShuffleList[i-1][j] == " ":
                    ShuffleList[i][j],ShuffleList[i-1][j] = ShuffleList[i-1][j],ShuffleList[i][j]
                elif ShuffleList[i+1][j] == " ":
                    ShuffleList[i][j],ShuffleList[i+1][j] = ShuffleList[i+1][j],ShuffleList[i][j]




        self.ButtonGrid()
        if ShuffleList[0] == [1,2,3,4] and ShuffleList[1] == [5,6,7,8] and ShuffleList[2] == [9,10,11,12] and ShuffleList[3]==[13,14,15," "]:
            self.ChangeColor()




        print(ShuffleList)
        #self.MyGrid[i][j]['text'] = "hello"


def RandomNumGen():

    NumberList = []
    NewNumList = []
    ctr = 0
    while ctr <= 15:
        num = random.randint(0, 15)
        if num not in NumberList:
            if num == 0:
                pos = ctr
            NumberList.append(num)
            ctr += 1
    NumberList[pos] = " "
    #print(NumberList)

    NewNumList.append(NumberList[0:4])
    NewNumList.append(NumberList[4:8])
    NewNumList.append(NumberList[8:12])
    NewNumList.append(NumberList[12:])

    return NewNumList


ShuffleMain = Tk()
ShuffleMain.title("LETS SHUFFLE")

ShuffleList = []

ShuffleGame = ST(ShuffleMain)
ShuffleList = RandomNumGen()
print(ShuffleList)
ShuffleGame.ButtonGrid()

ShuffleMain.mainloop()
