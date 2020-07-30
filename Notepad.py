#GUI Notepad

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file

    file = askopenfilename(defaultextension = ".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)

        f = open(file, "r")
        TextArea.insert(1.0,f.read())

        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension = ".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            #Save it as a New File
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad k bhaare meh ky hi bholu")


if __name__ == '__main__':
    #Basic Tkinter Setup
    root = Tk()
    root.title("Untitled - Notepad")
    #root.wm_iconbitmap("")
    root.geometry("500x600")

    TextArea = Text(root, font = "lucida 13")
    file = None
    TextArea.pack(expand = True, fill = BOTH)

    #Creating a Menu Bar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff = 0)

    #To open a New File
    FileMenu.add_command(label = "New", command = newFile)

    #To open already existing File
    FileMenu.add_command(label = "Open", command = openFile)

    #To save the current file
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)

    MenuBar.add_cascade(label = "File", menu = FileMenu)

    root.config(menu = MenuBar)

    #Adding Scrollbar using rules from tkinter
    scroll = Scrollbar(TextArea)
    scroll.pack(side = RIGHT, fill = Y)
    scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = scroll.set)



    #Edit Menu
    EditMenu = Menu(MenuBar, tearoff = 0)
    #To give a feature of Cut, Copy, Paste
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label = "Copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)

    MenuBar.add_cascade(label = "Edit", menu = EditMenu)

    #Help Menu
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command = about)

    MenuBar.add_cascade(label = "Help", menu = HelpMenu)


    #line_col = StringVar()
    #line_col.set("Line 1, col 1")

    statusvar = Frame(root,relief = GROOVE).pack(side = BOTTOM , fill =X)

    Label(statusvar,text= "Ready",width =18).pack(side = RIGHT)
    Label(statusvar,text= "Windows",width =18).pack(side = LEFT)
    #Label(statusvar,textvariable =line_col, width=20).pack(side=RIGHT)
    Label(statusvar, text="UTF-5", width=18).pack(side=RIGHT)
    







    root.mainloop()


