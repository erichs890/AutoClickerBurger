from AutoClicker import *
from tkinter import *
def fechar():
    janela.quit()
janela = Tk()
janela.geometry('300x300')
janela.title("Auto Clicker Burger")
Titulo = Label(text= "AutoClicker foda \n Aperte o botão direito do mouse para parar. \n Certifique-se que o jogo está em seu proximo alt tab.")
Titulo.pack()
Fodastico = Button(text="Clicar infinitamente", command= clicarInfinitamente)
Fodastico.pack()
Gatinho = Button(text="Alimentar o gato", command=alimentarGato)
Gatinho.pack()
FecharBtn = Button(janela, text="Fechar o aplicativo", command=fechar)
FecharBtn.pack()
Creditos = Label(text="Desenvolvido por Erich Schlaepfer")
Creditos.pack(side='bottom')
janela.mainloop()
