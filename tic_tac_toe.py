from tkinter import Tk, Button,Label,messagebox
root = Tk()
root.title("Simple GUI")


def dissable_buttons():
  b1.config(state="disabled")
  b2.config(state="disabled")
  b3.config(state="disabled")
  b4.config(state="disabled")
  b5.config(state="disabled")
  b6.config(state="disabled")
  b7.config(state="disabled")
  b8.config(state="disabled")
  b9.config(state="disabled")
#fun.  to check winning
def check_win():
  global winner
  winner=False
  #checking for x win
  if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
    b1.config(bg="green")
    b2.config(bg="green")
    b3.config(bg="green")
    winner=True
    messagebox.showinfo("X wins")
    dissable_buttons()
  elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
    b4.config(bg="green")
    b5.config(bg="green")
    b6.config(bg="green")
    winner=True
    messagebox.showinfo("X wins")
    dissable_buttons()
  elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
    b7.config(bg="green")
    b8.config(bg="green")
    b9.config(bg="green")
    winner=True
    messagebox.showinfo("X wins")
    dissable_buttons()
  elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
    b1.config(bg="green")
    b4.config(bg="green")
    b7.config(bg="green")
    winner=True
    messagebox.showinfo("X wins")
    dissable_buttons()
  elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
    b2.config(bg="green")
    b5.config(bg="green")
    b8.config(bg="green")
    winner=True
    messagebox.showinfo("X wins")
    dissable_buttons()
  elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
    b3.config(bg="green")
    b6.config(bg="green")
    b9.config(bg="green")
    winner=True
    messagebox.showinfo("X wins")
    dissable_buttons()  
  elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
    b1.config(bg="green")
    b5.config(bg="green")
    b9.config(bg="green")
    winner=True
    messagebox.showinfo("X wins")
    dissable_buttons()
  elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
    b3.config(bg="green")
    b5.config(bg="green")
    b7.config(bg="green")
    winner=True
    messagebox.showinfo("X wins")
    dissable_buttons()

  #checking for y win
  elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
    b1.config(bg="green")
    b2.config(bg="green")
    b3.config(bg="green")
    winner=True
    messagebox.showinfo("O wins")
    dissable_buttons()
  elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
    b4.config(bg="green")
    b5.config(bg="green")
    b6.config(bg="green")
    winner=True
    messagebox.showinfo("O wins")
    dissable_buttons()
  elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
    b7.config(bg="green")
    b8.config(bg="green")
    b9.config(bg="green")
    winner=True
    messagebox.showinfo("O wins")
    dissable_buttons()
  elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
    b1.config(bg="green")
    b4.config(bg="green")
    b7.config(bg="green")
    winner=True
    messagebox.showinfo("O wins")
    dissable_buttons()
  elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
    b2.config(bg="green")
    b5.config(bg="green")
    b8.config(bg="green")
    winner=True
    messagebox.showinfo("O wins")
    dissable_buttons()
  elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
    b3.config(bg="green")
    b6.config(bg="green")
    b9.config(bg="green")
    winner=True
    messagebox.showinfo("O wins")
    dissable_buttons()  
  elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
    b1.config(bg="green")
    b5.config(bg="green")
    b9.config(bg="green")
    winner=True
    messagebox.showinfo("O wins")
    dissable_buttons()
  elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
    b3.config(bg="green")
    b5.config(bg="green")
    b7.config(bg="green")
    winner=True
    messagebox.showinfo("O wins")
    dissable_buttons()
  

  #declairing global variable
clk =True
count = 0

#function for  button clicking
def button_clicked(b):
  global clk,count
  if b["text"] == "" and clk==True:
    b["text"]="X"
    clk=False
    count=count+1
    check_win()
  elif b["text"] == "" and clk==False:
    b["text"]="O"
    clk=True
    count=count+1
    check_win()
  else:
    messagebox.showerror("this is already filled")
 
  
#buttons creation: 

b1=Button(root, font=("calibri",20), height=3,width=6,background="white",command=lambda:button_clicked(b1))
b2=Button(root, font=("calibri",20), height=3,width=6,background="white",command=lambda:button_clicked(b2))
b3=Button(root, font=("calibri",20), height=3,width=6,background="white",command=lambda:button_clicked(b3))
b4=Button(root, font=("calibri",20), height=3,width=6,background="white",command=lambda:button_clicked(b4))
b5=Button(root, font=("calibri",20), height=3,width=6,background="white",command=lambda:button_clicked(b5))
b6=Button(root, font=("calibri",20), height=3,width=6,background="white",command=lambda:button_clicked(b6))
b7=Button(root, font=("calibri",20), height=3,width=6,background="white",command=lambda:button_clicked(b7))
b8=Button(root, font=("calibri",20), height=3,width=6,background="white",command=lambda:button_clicked(b8))
b9=Button(root, font=("calibri",20), height=3,width=6,background="white",command=lambda:button_clicked(b9))
#grid our buttons
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

root.mainloop()