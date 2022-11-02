from tkinter import *
from tkinter import ttk


#cores

cor1 = "#1e1f1e" #preta

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)

janela.mainloop()

