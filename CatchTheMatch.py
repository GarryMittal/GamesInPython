from tkinter import *
from PIL import Image,ImageTk
import time
import random
from tkinter import messagebox

def RandomImg():

    random.shuffle(ImgObjList)
    return ImgObjList

class CTM:
    def __init__(self,CatchMain):
        self.main = CatchMain
        self.frame = Frame(self.main)
        self.frame.grid(row=0)
    def buttongrid(self):

        self.mygrid=[]
        for x in range(0,4):
            row=[]
            for y in range(0,4):
                row.append(Button(self.frame,image=Blank,height=150,width=150,command=lambda i=x,j=y:self.MemoryClick(i,j)))
                row[-1].grid(row=x,column=y)
            self.mygrid.append(row)

    def PutImage(self,i,j):
        self.mygrid[i][j]['image'] = GameList[i][j]

    def MemoryClick(self,i,j):
        tup=(i,j)
        self.PutImage(i,j)

        #self.mygrid[i][j]['image'] = GameList[i][j]
        if tup not in ButtonList:

            ButtonList.append(tup)
            MemoryList.append(GameList[i][j])
        #time.sleep(1)
        if len(MemoryList)%2 != 0 and len(MemoryList)>1:

            if MemoryList[-2] != MemoryList[-3]:
                del MemoryList[-3:-1]
                ToBlank1 = ButtonList[-2]
                self.mygrid[ToBlank1[0]][ToBlank1[1]]['image'] = Blank
                ToBlank2 = ButtonList[-3]
                self.mygrid[ToBlank2[0]][ToBlank2[1]]['image'] = Blank
                del ButtonList[-3:-1]

        print(ButtonList)
        if len(ButtonList) == 16:
            messagebox.showinfo("VICTORY","You Won")



ctr=0
CatchMain = Tk()

BlankImage1 = Image.open("D:\\Python-GUI\\Project XO\\Images\\Blank.png")
BlankImage1.resize((50,50))
Blank = ImageTk.PhotoImage(BlankImage1)

image1 = Image.open("D:\\Python-GUI\\Project XO\\Images\\anaconda.jpg")
image1 = image1.resize((50,50))
img1 = ImageTk.PhotoImage(image1)

image2 = Image.open("D:\\Python-GUI\\Project XO\\Images\\coding.png")
image2 = image2.resize((50,50))
img2 = ImageTk.PhotoImage(image2)

image3 = Image.open("D:\\Python-GUI\\Project XO\\Images\\CSS.jpg")
image3 = image3.resize((50,50))
img3 = ImageTk.PhotoImage(image3)

image4 = Image.open("D:\\Python-GUI\\Project XO\\Images\\javalogo.png")
image4 = image4.resize((50,50))
img4 = ImageTk.PhotoImage(image4)

image5 = Image.open("D:\\Python-GUI\\Project XO\\Images\\javascriptlogo.jpg")
image5 = image5.resize((50,50))
img5 = ImageTk.PhotoImage(image5)

image6 = Image.open("D:\\Python-GUI\\Project XO\\Images\\mysql.png")
image6 = image6.resize((50,50))
img6 = ImageTk.PhotoImage(image6)

image7 = Image.open("D:\\Python-GUI\\Project XO\\Images\\phplogo.png")
image7 = image7.resize((50,50))
img7 = ImageTk.PhotoImage(image7)

image8 = Image.open("D:\\Python-GUI\\Project XO\\Images\\pythonlogo.png")
image8 = image8.resize((50,50))
img8 = ImageTk.PhotoImage(image8)

ImgObjList = [img1,img2,img3,img4,img5,img6,img7,img8,img1,img2,img3,img4,img5,img6,img7,img8]

GameList  = []
TraceList = RandomImg()
print(len(TraceList))
GameList.append(TraceList[0:4])
GameList.append(TraceList[4:8])
GameList.append(TraceList[8:12])
GameList.append(TraceList[12:])
print(len(GameList))
MemoryList = []
ButtonList=[]
CatchObj = CTM(CatchMain)
CatchObj.buttongrid()
CatchMain.mainloop()
'''
MainBgColor = "#3c91e6"
MainW = Tk()
MainW.config(bg = MainBgColor)
MainW.title("XO WORLD WELCOMES YOU")
MainW.geometry("500x500")
canvas = Canvas(MainW,height = 500, width = 500)
canvas.config(bg = MainBgColor)
canvas.pack()

EmptyFrame = Frame(canvas,padx=30,pady=10,height=50,width=60,bg=MainBgColor)

#EmptyFrame.config()
EmptyFrame.pack(expand=True,fill=X)

GameFrame = Frame(canvas,padx=30,pady=10)
GameFrame.config(bg = MainBgColor)
GameFrame.pack()
NewGameButton = Button(GameFrame,text = "GAME XO",command = NewGame,width=20,height=2)
NewGameButton.grid(row=4,column=3)

#NewGameButton.pack()

GameFrame2 = Frame(canvas,padx=30,pady=10)
GameFrame2.config(bg=MainBgColor)
GameFrame2.pack()
ShuffleTruffle = Button(GameFrame2,text="SHUFFLE TRUFFLE",command = ShuffleTruffleGame,width=20,height=2)
ShuffleTruffle.pack()

MainW.mainloop()
'''
