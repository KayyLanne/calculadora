from tkinter import *
from tkinter import ttk


#cores

cor1 = "#1e1f1e" #preta
cor2 = "#feffff" #branco
cor3 = "#38576b" #Azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

#criando as partes das telas

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#Criando os botôes

b1 = Button(frame_corpo, text="C", width=11, height=2)
b1.place(x=0, y=0)

b2 = Button(frame_corpo, text="%", width=11, height=2)
b2.place(x=80, y=0)

b3 = Button(frame_corpo, text="/", width=11, height=2, bg=cor5)
b3.place(x=150, y=0)

janela.mainloop()

