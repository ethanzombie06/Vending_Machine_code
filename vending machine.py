import tkinter




class poggers:

    def addtobasket(self):
        self.basketwindow = tkinter.Toplevel(self.root)
        self.basketwindow.title("basket")
        self.basketwindow.geometry("100x70")
        
        self.basketlbl=tkinter.Label(self.basketwindow,text=("{} Sandwichs\n{} Crisps\n{} Milkyways\n{} kitkats".format(self.nSandwich,self.crisps,self.milkyway,self.kitkat)))
        self.basketlbl.place(x=25,y=0)

    def FinishedOrder(self):
        self.orderwin = tkinter.Toplevel(self.root)
        self.orderwin.title("confirm order")
        self.orderwin.geometry("160x70")
        nFinalCost = ((self.nSandwich*3)+(self.crisps*2)+(self.milkyway*1.5)+(self.kitkat*1.5))
        self.totalcost=tkinter.Label(self.orderwin,text =("your order will cost: £{}".format(nFinalCost)))
        self.totalcost.place(x=5,y=10)
        self.end = tkinter.Button(self.orderwin,text=("confirm"))
        self.end.place(x=50, y= 40)


    def gettxt(self):
        entered_txt = self.textbox.get()
        try:
            if entered_txt == "1":
                self.nSandwich += 1
            if entered_txt == "2":
                self.crisps += 1
            if entered_txt == "3":
                self.milkyway += 1
            if entered_txt == "4":
                self.kitkat += 1

            else:
                pass
        except(Exception):
            pass

    def __init__(self,root):

        self.root = root
        self.basket =[]
        self.root.geometry("203x200")
        
        self.nSandwich = (0)
        self.crisps = (0)
        self.milkyway = (0)
        self.kitkat = (0)

        self.textbox()
        self.getTxtButton()
        self.exitButton()
        self.menu()
        self.updateorder()
        self.order()
        
    def exitButton(self):
        self.ExitButton=tkinter.Button(self.root,text="exit",command=lambda: self.root.quit())
        self.ExitButton.place(x=173, y=0)

    def getTxtButton(self):
        self.EnterButton=tkinter.Button(self.root,text="enter",command=(self.gettxt))
        self.EnterButton.place(x=0,y=0)

    def textbox(self):
        self.textbox = tkinter.Entry(self.root,width=20,bg="grey")
        self.textbox.place(x=44, y=5)
    def menu(self):
        self.menulist=tkinter.Label(self.root, text="MENU\n 1   sandwich    £3\n 2   crisps    £2\n 3   milkyway   £1.50\n 4   kitkat   £1.50")
        self.menulist.place(x=50,y=65)

    def updateorder(self):
        self.viewbasket=self.EnterButton=tkinter.Button(self.root,text="view order",command=(self.addtobasket))
        self.viewbasket.place(x=70,y=30)
    def order(self):
        self.finsh=tkinter.Button(self.root,text="finish order",command=(self.FinishedOrder))
        self.finsh.place(x=68,y=150)

if(__name__ == "__main__"):
    tk = tkinter.Tk()
    pog = poggers(tk)
    tk.mainloop()
    