import tkinter as tk
from tkinter import *
from Dados import Dados


class EscArqView:
    def __init__(self, master):
        self.master = master

        self.container1 = tk.Frame(self.master, pady = 10)
        self.lblCabecalho = tk.Label(self.container1, text = "Digite os dados abaixo")
        self.lblCabecalho.pack()
        self.container1.pack()

        self.container2 = tk.Frame(self.master, pady = 5, padx = 20)
        self.lblNome = tk.Label(self.container2, text = "Nome:", width = 10)
        self.entryNome = tk.Entry(self.container2)
        self.container2.pack()
        self.lblNome.pack(side=LEFT)
        self.entryNome.pack()

        self.container3 = tk.Frame(self.master, pady = 5, padx = 20)
        self.lblCPF = tk.Label(self.container3, text = "CPF:", width = 10)
        self.entryCPF = tk.Entry(self.container3)
        self.container3.pack()
        self.lblCPF.pack(side=LEFT)
        self.entryCPF.pack()

        self.container4 = tk.Frame(self.master, pady = 5, padx = 20)
        self.lblFONE = tk.Label(self.container4, text = "Telefone:", width = 10)
        self.entryFONE = tk.Entry(self.container4)
        self.container4.pack()
        self.lblFONE.pack(side=LEFT)
        self.entryFONE.pack()

        self.container5 = tk.Frame(self.master, pady = 4, padx = 20)
        self.btnSubmeter = tk.Button(self.container5, text = "Submmit", width = 12, command = self.submmit)
        self.btnSubmeter.pack(side = LEFT)
        self.container5.pack(side = RIGHT)

        self.container6 = tk.Frame(self.master, pady = 4, padx = 20)
        self.lblmsg = tk.Label(self.container6, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
        self.container6.pack()

    def submmit(self):
       	dados = Dados()

       	dados.nome = self.entryNome.get()
        dados.cpf = self.entryCPF.get()
        dados.telefone = self.entryFONE.get()
   
        print(dados.nome, dados.cpf, dados.telefone)

        self.lblmsg["text"] = dados.insertUser()


    	#submissão ao arquivo csv
       	f = open("teste.csv", "r")

       	conteudo = []
       	conteudo = f.readlines()

       	if not conteudo:
       		conteudo.append("nome, cpf, telefone \n")	

       	conteudo.append(self.entryNome.get() + ", ")
       	conteudo.append(self.entryCPF.get() + ", ")
       	conteudo.append(self.entryFONE.get() + "\n")

       	f = open("teste.csv", "w")

       	f.writelines(conteudo)
       	f.close


    def close_windows(self):
        self.master.destroy()
