from tkinter import *
class Calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = entDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
            self.display(self.current)

    def display(self, value):
        entDisplay.delete(0, END)
        entDisplay.insert(0, value)

    def clear_entry(self):
        self.current = "0"
        self.display(self.current)
        self.input_value = True

    def clear_all(self):
        self.clear_entry()
        self.total = 0

    def clear_last(self):
        self.current = self.current[:-1]
        self.display(self.current)

added_value = Calculator()
root = Tk()
blank_space = " "
root.title(50 * blank_space + "My Calculator")
root.resizable(width=False, height=False)
root.geometry("438x573+460+40")

coverFrame = Frame(root, bd=20, pady=2, relief=RIDGE)
coverFrame.grid()

coverMainFrame = Frame(coverFrame, bd=10, pady=2, bg='royalblue', relief=RIDGE)
coverMainFrame.grid()

MainFrame = Frame(coverMainFrame, bd=5, pady=2, relief=RIDGE)
MainFrame.grid()

entDisplay = Entry(MainFrame, font=('arial', 18, 'bold'), bd=14, width=26, bg='royalblue', justify=RIGHT)
entDisplay.grid(row=0, column=0, columnspan=4, pady=1)
entDisplay.insert(0, "0")

numpad = "789456123"
i = 0
btn = []

for j in range(3, 6):
    for k in range(3):
        btn.append(Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=numpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numpad[i]: added_value.numberEnter(x)
        i += 1

btnBackSpace = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="←", bg='royalblue', command=added_value.clear_last)
btnBackSpace.grid(row=1, column=0, pady=1)

btnClear = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(67), bg='royalblue', command=added_value.clear_entry)
btnClear.grid(row=1, column=1, pady=1)

btnClearAll = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(67) + chr(69), bg='royalblue', command=added_value.clear_all)
btnClearAll.grid(row=1, column=2, pady=1)

btnPM = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(177), bg='royalblue')
btnPM.grid(row=1, column=3, pady=1)

btnSq = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="√")
btnSq.grid(row=2, column=0, pady=1)

btnCos = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="Cos")
btnCos.grid(row=2, column=1, pady=1)

btntan = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="Tan")
btntan.grid(row=2, column=2, pady=1)

btnsin = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="Sin", bg='royalblue')
btnsin.grid(row=2, column=3, pady=1)

btnAdd = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="+", bg="royalblue")
btnAdd.grid(row=3, column=3, pady=1)

btnSub = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="-", bg="royalblue")
btnSub.grid(row=4, column=3, pady=1)

btnMult = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="*", bg="royalblue")
btnMult.grid(row=5, column=3, pady=1)

btnDiv = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=chr(247), bg="royalblue")
btnDiv.grid(row=6, column=3, pady=1)

btnZero = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="0", bg="royalblue")
btnZero.grid(row=6, column=0, pady=1)

btnDot = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text=".", bg="royalblue")
btnDot.grid(row=6, column=1, pady=1)

btnEquals = Button(MainFrame, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text="=", bg="royalblue")
btnEquals.grid(row=6, column=2, pady=1)

root.mainloop()
