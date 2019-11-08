from tkinter import *
from tkinter import font
import random
import winsound

class Batalha_Naval:
    #Janela inicial
    def __init__(self,Janela):
        global tiro_navio,tiro_bomba,tiro_agua
        tiro_navio="Acerto"
        tiro_bomba="Bomba"
        tiro_agua="Agua"
        self.voltar=0
        self.fontes = [font.Font(family="Fluo Gums", size=20), font.Font(family="Fluo Gums", size=10), font.Font(family="Fluo Gums", size=9),font.Font(family="Fluo Gums", size=7)]
        self.lb_batalha=Label(Janela, text="BATALHA NAVAL", fg="blue", font=self.fontes[0])
        self.lb_batalha.place(x=50,y=50)
        self.bt_jogar = Button(Janela, text="JOGAR", fg="blue", activeforeground="blue", command=self.dificuldade, font=self.fontes[1], relief=FLAT)
        self.bt_jogar.place(x=210, y=200)
        self.bt_sair=Button(Janela,text="SAIR",fg="blue", activeforeground="blue", command=self.fechar, font=self.fontes[1], relief=FLAT)
        self.bt_sair.place(x=220,y=250)     

    def fechar(self):
        winsound.PlaySound("Vazio",winsound.SND_PURGE)
        Janela.destroy()
        
    def dificuldade(self):
        Janela.geometry('500x400+450+150')
        #Apagando widgets
        if self.voltar>=1:
            winsound.PlaySound("Janela_inicial",winsound.SND_ASYNC|winsound.SND_LOOP)
            self.bt_jogar_novamente.place_forget()
            self.txt_jan_final.place_forget()
            
        self.lb_batalha.place_forget()
        self.bt_jogar.place_forget()
        self.bt_sair.place_forget()
        #Botões de nivel
        self.como_jogar=Label(Janela,text="COMO JOGAR:",font=self.fontes[0],fg="blue")
        self.como_jogar.place(x=25, y=10)
        self.txt_como_jogar=Label(Janela,justify=LEFT,text="SEMELHANTE AO JOGO CAMPO MINADO, O JOGADOR DEVE\nACERTAR TODOS OS BARCOS CLICANDO NO TABULEIRO SEM QUE\nSUAS VIDAS SEJAM IGUALADAS A ZERO. A QUANTIDADE DE\nBARCOS VARIA DE ACORDO COM O NIVEL ESCOLHIDO PELO\nUSUARIO.MAS CUIDADO, POIS VOCE SO POSSUI 3 VIDAS.",font=self.fontes[3],fg="#6495ED")
        self.txt_como_jogar.place(x=25,y=75)
        
        self.selecione=Label(Janela,text="SELECIONE UM NIVEL ABAIXO:",font=self.fontes[1],fg="blue")
        self.selecione.place(x=25,y=250)
        self.bt_facil=Button(Janela, text="FACIL", command= lambda: self.jan_jogo(1),font=self.fontes[2],fg="#6495ED",activeforeground="#6495ED", relief=FLAT)
        self.bt_facil.place(x=25,y=280)
        self.bt_medio = Button(Janela, text="MEDIO", command= lambda: self.jan_jogo(2),font=self.fontes[2],fg="#6495ED",activeforeground="#6495ED", relief=FLAT)
        self.bt_medio.place(x=100,y=280)
        self.bt_dificil = Button(Janela,text="DIFICIL", command=lambda: self.jan_jogo(3),font=self.fontes[2],fg="#6495ED",activeforeground="#6495ED", relief=FLAT)
        self.bt_dificil.place(x=175,y=280)

    def bt_navio(self, i, j,posi_x,posi_y):
        def navio_horizontal_0():
            if i-1<0 and j-1>=0:
                self.bt[i][j-1]["bg"]="blue"
                self.bt[i][j-1]["state"]=DISABLED
                self.bt[i+1][j-1]["bg"]="blue"
                self.bt[i+1][j-1]["state"]=DISABLED
            if i+1>len(self.tabuleiro)-1 and j-1>=0:
                self.bt[i][j-1]["bg"]="blue"
                self.bt[i][j-1]["state"]=DISABLED
                self.bt[i-1][j-1]["bg"]="blue"
                self.bt[i-1][j-1]["state"]=DISABLED
            if (i+1<=len(self.tabuleiro)-1 and j+1<=len(self.tabuleiro)-1) and (i-1>=0 and j-1>=0):
                self.bt[i-1][j-1]["bg"]="blue"
                self.bt[i-1][j-1]["state"]=DISABLED
                self.bt[i][j-1]["bg"]="blue"
                self.bt[i][j-1]["state"]=DISABLED
                self.bt[i+1][j-1]["bg"]="blue"
                self.bt[i+1][j-1]["state"]=DISABLED
                
        def navio_horizontal_1():
            if i-1<0 and j+1<=len(self.tabuleiro)-1:
                self.bt[i][j+1]["bg"]="blue"
                self.bt[i][j+1]["state"]=DISABLED
                self.bt[i+1][j+1]["bg"]="blue"
                self.bt[i+1][j+1]["state"]=DISABLED
            if i+1>len(self.tabuleiro)-1 and j+1<=len(self.tabuleiro)-1:
                self.bt[i][j+1]["bg"]="blue"
                self.bt[i][j+1]["state"]=DISABLED
                self.bt[i-1][j+1]["bg"]="blue"
                self.bt[i-1][j+1]["state"]=DISABLED
            if (i+1<=len(self.tabuleiro)-1 and j+1<=len(self.tabuleiro)-1) and (i-1>=0 and j-1>=0): 
                self.bt[i-1][j+1]["bg"]="blue"
                self.bt[i-1][j+1]["state"]=DISABLED
                self.bt[i][j+1]["bg"]="blue"
                self.bt[i][j+1]["state"]=DISABLED
                self.bt[i+1][j+1]["bg"]="blue"
                self.bt[i+1][j+1]["state"]=DISABLED

        def navio_vertical_0():
            if j-1<0 and i-1>=0:
                self.bt[i-1][j]["bg"]="blue"
                self.bt[i-1][j]["state"]=DISABLED
                self.bt[i-1][j+1]["bg"]="blue"
                self.bt[i-1][j+1]["state"]=DISABLED
            if j+1>len(self.tabuleiro)-1 and i-1>=0:
                self.bt[i-1][j-1]["bg"]="blue"
                self.bt[i-1][j-1]["state"]=DISABLED
                self.bt[i-1][j]["bg"]="blue"
                self.bt[i-1][j]["state"]=DISABLED
            if (j+1<=len(self.tabuleiro)-1 and i+1<=len(self.tabuleiro)-1) and (j-1>=0 and i-1>=0):
                self.bt[i-1][j-1]["bg"]="blue"
                self.bt[i-1][j-1]["state"]=DISABLED
                self.bt[i-1][j]["bg"]="blue"
                self.bt[i-1][j]["state"]=DISABLED
                self.bt[i-1][j+1]["bg"]="blue"
                self.bt[i-1][j+1]["state"]=DISABLED
        def navio_vertical_1():
            if j-1<0 and i+1<=len(self.tabuleiro)-1:
                self.bt[i+1][j]["bg"]="blue"
                self.bt[i+1][j]["state"]=DISABLED
                self.bt[i+1][j+1]["bg"]="blue"
                self.bt[i+1][j+1]["state"]=DISABLED
            if j+1>len(self.tabuleiro)-1 and i+1<=len(self.tabuleiro)-1:
                self.bt[i+1][j-1]["bg"]="blue"
                self.bt[i+1][j-1]["state"]=DISABLED
                self.bt[i+1][j]["bg"]="blue"
                self.bt[i+1][j]["state"]=DISABLED
            if (j+1<=len(self.tabuleiro)-1 and i+1<=len(self.tabuleiro)-1) and (j-1>=0 and i-1>=0): 
                self.bt[i+1][j-1]["bg"]="blue"
                self.bt[i+1][j-1]["state"]=DISABLED
                self.bt[i+1][j]["bg"]="blue"
                self.bt[i+1][j]["state"]=DISABLED
                self.bt[i+1][j+1]["bg"]="blue"
                self.bt[i+1][j+1]["state"]=DISABLED
            
        self.navio_clicado_1 = 0
        self.navio_clicado_2 = 0
        self.navio_clicado_3 = 0
        self.navio_clicado_4 = 0
        self.navio_clicado_5 = 0
        self.vida=3
        #Ação a ser realizada, quando o botão "N" for clicado
        def clique_navio():
            if self.tabuleiro[i][j]=="1":
                winsound.PlaySound(tiro_navio,winsound.SND_ASYNC)
                self.navio_clicado_1+=1
                self.bt[i][j]["bg"]="#FFD700"
                self.bt[i][j]["state"]=DISABLED
                self.txt_vidas["fg"]="#008B8B"
                #Botões ao redor
                    
                if j-1<0 and i-1<0:
                    self.bt[i][j+1]["bg"]="blue"
                    self.bt[i][j+1]["state"]=DISABLED
                    self.bt[i+1][j]["bg"]="blue"
                    self.bt[i+1][j]["state"]=DISABLED
                    self.bt[i+1][j+1]["bg"]="blue"
                    self.bt[i+1][j+1]["state"]=DISABLED

                elif j+1>len(self.tabuleiro)-1 and i+1>len(self.tabuleiro)-1:
                    self.bt[i-1][j]["bg"]="blue"
                    self.bt[i-1][j]["state"]=DISABLED
                    self.bt[i-1][j-1]["bg"]="blue"
                    self.bt[i-1][j-1]["state"]=DISABLED
                    self.bt[i][j-1]["bg"]="blue"
                    self.bt[i][j-1]["state"]=DISABLED
                    
                elif j-1<0 and i+1>len(self.tabuleiro)-1:
                    self.bt[i][j+1]["bg"]="blue"
                    self.bt[i][j+1]["state"]=DISABLED
                    self.bt[i-1][j]["bg"]="blue"
                    self.bt[i-1][j]["state"]=DISABLED
                    self.bt[i-1][j+1]["bg"]="blue"
                    self.bt[i-1][j+1]["state"]=DISABLED
                    
                elif j+1>len(self.tabuleiro)-1 and i-1<0:
                    self.bt[i][j-1]["bg"]="blue"
                    self.bt[i][j-1]["state"]=DISABLED
                    self.bt[i+1][j-1]["bg"]="blue"
                    self.bt[i+1][j-1]["state"]=DISABLED
                    self.bt[i+1][j]["bg"]="blue"
                    self.bt[i+1][j]["state"]=DISABLED

                elif i-1<0:
                    self.bt[i][j-1]["bg"]="blue"
                    self.bt[i][j-1]["state"]=DISABLED
                    self.bt[i][j+1]["bg"]="blue"
                    self.bt[i][j+1]["state"]=DISABLED
                    self.bt[i+1][j-1]["bg"]="blue"
                    self.bt[i+1][j-1]["state"]=DISABLED
                    self.bt[i+1][j]["bg"]="blue"
                    self.bt[i+1][j]["state"]=DISABLED
                    self.bt[i+1][j+1]["bg"]="blue"
                    self.bt[i+1][j+1]["state"]=DISABLED
                elif j-1<0:
                    self.bt[i-1][j]["bg"]="blue"
                    self.bt[i-1][j]["state"]=DISABLED
                    self.bt[i-1][j+1]["bg"]="blue"
                    self.bt[i-1][j+1]["state"]=DISABLED
                    self.bt[i][j+1]["bg"]="blue"
                    self.bt[i][j+1]["state"]=DISABLED
                    self.bt[i+1][j]["bg"]="blue"
                    self.bt[i+1][j]["state"]=DISABLED
                    self.bt[i+1][j+1]["bg"]="blue"
                    self.bt[i+1][j+1]["state"]=DISABLED
                    
                elif i+1>len(self.tabuleiro)-1:
                    self.bt[i-1][j-1]["bg"]="blue"
                    self.bt[i-1][j-1]["state"]=DISABLED
                    self.bt[i-1][j]["bg"]="blue"
                    self.bt[i-1][j]["state"]=DISABLED
                    self.bt[i-1][j+1]["bg"]="blue"
                    self.bt[i-1][j+1]["state"]=DISABLED
                    self.bt[i][j-1]["bg"]="blue"
                    self.bt[i][j-1]["state"]=DISABLED
                    self.bt[i][j+1]["bg"]="blue"
                    self.bt[i][j+1]["state"]=DISABLED
                    
                elif j+1>len(self.tabuleiro)-1:
                    self.bt[i-1][j-1]["bg"]="blue"
                    self.bt[i-1][j-1]["state"]=DISABLED
                    self.bt[i-1][j]["bg"]="blue"
                    self.bt[i-1][j]["state"]=DISABLED
                    self.bt[i][j-1]["bg"]="blue"
                    self.bt[i][j-1]["state"]=DISABLED
                    self.bt[i+1][j-1]["bg"]="blue"
                    self.bt[i+1][j-1]["state"]=DISABLED
                    self.bt[i+1][j]["bg"]="blue"
                    self.bt[i+1][j]["state"]=DISABLED
                    
                elif (i-1>=0 and i+1<=len(self.tabuleiro)-1) and (j-1>=0 and j+1<=len(self.tabuleiro)-1):    
                    self.bt[i-1][j-1]["bg"]="blue"
                    self.bt[i-1][j-1]["state"]=DISABLED
                    self.bt[i-1][j]["bg"]="blue"
                    self.bt[i-1][j]["state"]=DISABLED
                    self.bt[i-1][j+1]["bg"]="blue"
                    self.bt[i-1][j+1]["state"]=DISABLED
                    self.bt[i][j-1]["bg"]="blue"
                    self.bt[i][j-1]["state"]=DISABLED
                    self.bt[i][j+1]["bg"]="blue"
                    self.bt[i][j+1]["state"]=DISABLED
                    self.bt[i+1][j-1]["bg"]="blue"
                    self.bt[i+1][j-1]["state"]=DISABLED
                    self.bt[i+1][j]["bg"]="blue"
                    self.bt[i+1][j]["state"]=DISABLED
                    self.bt[i+1][j+1]["bg"]="blue"
                    self.bt[i+1][j+1]["state"]=DISABLED
                    
                if self.navio_clicado_1==1:
                    self.bt_navio1["bg"]="#A9A9A9"
                    self.txt_navio1["fg"]="#A9A9A9"
                    
            if self.tabuleiro[i][j]=="2":
                winsound.PlaySound(tiro_navio,winsound.SND_ASYNC)
                self.navio_clicado_2 += 1
                self.bt[i][j]["bg"]="#228B22"
                self.bt[i][j]["state"]=DISABLED
                self.txt_vidas["fg"]="#008B8B"
                
                #Botões ao redor horizontal
                if self.vertica_horizontal_2==0:
                    if j==navio_2_horizontal[0]:
                        navio_horizontal_0()
                    if j==navio_2_horizontal[-1]:
                        navio_horizontal_1()        
                    if i+1>len(self.tabuleiro)-1:
                        self.bt[i-1][j]["bg"]="blue"
                        self.bt[i-1][j]["state"]=DISABLED
                    elif i-1<0:
                        self.bt[i+1][j]["bg"]="blue"
                        self.bt[i+1][j]["state"]=DISABLED
                    elif i+1<=len(self.tabuleiro)-1 and i-1>=0:
                        self.bt[i+1][j]["bg"]="blue"
                        self.bt[i+1][j]["state"]=DISABLED
                        self.bt[i-1][j]["bg"]="blue"
                        self.bt[i-1][j]["state"]=DISABLED

                #Botões ao redor vertical
                if self.vertica_horizontal_2==1:
                    if i==navio_2_vertical [0]:
                        navio_vertical_0()
                    if i==navio_2_vertical [-1]:
                        navio_vertical_1()
                    if j+1>len(self.tabuleiro)-1:
                        self.bt[i][j-1]["bg"]="blue"
                        self.bt[i][j-1]["state"]=DISABLED
                    elif j-1<0:
                        self.bt[i][j+1]["bg"]="blue"
                        self.bt[i][j+1]["state"]=DISABLED
                    elif j+1<=len(self.tabuleiro)-1 and j-1>=0:
                        self.bt[i][j+1]["bg"]="blue"
                        self.bt[i][j+1]["state"]=DISABLED
                        self.bt[i][j-1]["bg"]="blue"
                        self.bt[i][j-1]["state"]=DISABLED
                    
                if self.navio_clicado_2==2:
                    self.bt_navio2["bg"]="#A9A9A9"
                    self.txt_navio2["fg"]="#A9A9A9"
                    
            if self.tabuleiro[i][j]=="3":
                winsound.PlaySound(tiro_navio,winsound.SND_ASYNC)
                self.navio_clicado_3 += 1
                self.bt[i][j]["bg"]="#FFA500"
                self.bt[i][j]["state"]=DISABLED
                self.txt_vidas["fg"]="#008B8B"
                
                #Botões ao redor horizontal
                if self.vertica_horizontal_3==0:
                    if j==navio_3_horizontal[0]:
                        navio_horizontal_0()
                    if j==navio_3_horizontal[-1]:
                        navio_horizontal_1()
                    if i+1>len(self.tabuleiro)-1:
                        self.bt[i-1][j]["bg"]="blue"
                        self.bt[i-1][j]["state"]=DISABLED
                    elif i-1<0:
                        self.bt[i+1][j]["bg"]="blue"
                        self.bt[i+1][j]["state"]=DISABLED
                    elif i+1<=len(self.tabuleiro)-1 and i-1>=0:
                        self.bt[i+1][j]["bg"]="blue"
                        self.bt[i+1][j]["state"]=DISABLED
                        self.bt[i-1][j]["bg"]="blue"
                        self.bt[i-1][j]["state"]=DISABLED

                #Botões ao redor vertical
                if self.vertica_horizontal_3==1:
                    if i==navio_3_vertical [0]:
                        navio_vertical_0()
                    if i==navio_3_vertical [-1]:
                        navio_vertical_1()
                    if j+1>len(self.tabuleiro)-1:
                        self.bt[i][j-1]["bg"]="blue"
                        self.bt[i][j-1]["state"]=DISABLED
                    elif j-1<0:
                        self.bt[i][j+1]["bg"]="blue"
                        self.bt[i][j+1]["state"]=DISABLED
                    elif j+1<=len(self.tabuleiro)-1 and j-1>=0:
                        self.bt[i][j+1]["bg"]="blue"
                        self.bt[i][j+1]["state"]=DISABLED
                        self.bt[i][j-1]["bg"]="blue"
                        self.bt[i][j-1]["state"]=DISABLED
                        
                if self.navio_clicado_3==3:
                    self.bt_navio3["bg"]="#A9A9A9"
                    self.txt_navio3["fg"]="#A9A9A9"
                    
                
            if self.tabuleiro[i][j]=="4":
                winsound.PlaySound(tiro_navio,winsound.SND_ASYNC)
                self.navio_clicado_4 += 1
                self.bt[i][j]["bg"]="#9400D3"
                self.bt[i][j]["state"]=DISABLED
                self.txt_vidas["fg"]="#008B8B"
                
                #Botões ao redor horizontal
                if self.vertica_horizontal_4==0:
                    if j==navio_4_horizontal[0]:
                        navio_horizontal_0()
                    if j==navio_4_horizontal[-1]:
                        navio_horizontal_1()        
                    if i+1>len(self.tabuleiro)-1:
                        self.bt[i-1][j]["bg"]="blue"
                        self.bt[i-1][j]["state"]=DISABLED
                    elif i-1<0:
                        self.bt[i+1][j]["bg"]="blue"
                        self.bt[i+1][j]["state"]=DISABLED
                    elif i+1<=len(self.tabuleiro)-1 and i-1>=0:
                        self.bt[i+1][j]["bg"]="blue"
                        self.bt[i+1][j]["state"]=DISABLED
                        self.bt[i-1][j]["bg"]="blue"
                        self.bt[i-1][j]["state"]=DISABLED

                #Botões ao redor vertical
                if self.vertica_horizontal_4==1:
                    if i==navio_4_vertical [0]:
                        navio_vertical_0()
                    if i==navio_4_vertical [-1]:
                        navio_vertical_1()
                    if j+1>len(self.tabuleiro)-1:
                        self.bt[i][j-1]["bg"]="blue"
                        self.bt[i][j-1]["state"]=DISABLED
                    elif j-1<0:
                        self.bt[i][j+1]["bg"]="blue"
                        self.bt[i][j+1]["state"]=DISABLED
                    elif j+1<=len(self.tabuleiro)-1 and j-1>=0:
                        self.bt[i][j+1]["bg"]="blue"
                        self.bt[i][j+1]["state"]=DISABLED
                        self.bt[i][j-1]["bg"]="blue"
                        self.bt[i][j-1]["state"]=DISABLED
                        
                if self.navio_clicado_4==4:
                    self.bt_navio4["bg"]="#A9A9A9"
                    self.txt_navio4["fg"]="#A9A9A9"
                    
            if self.tabuleiro[i][j]=="5":
                winsound.PlaySound(tiro_navio,winsound.SND_ASYNC)
                self.navio_clicado_5 += 1
                self.bt[i][j]["bg"]="#2F4F4F"
                self.bt[i][j]["state"]=DISABLED
                self.txt_vidas["fg"]="#008B8B"
                
                #Botões ao redor horizontal
                if self.vertica_horizontal_5==0:
                    if j==navio_5_horizontal[0]:
                        navio_horizontal_0()
                    if j==navio_5_horizontal[-1]:
                        navio_horizontal_1()        
                    if i+1>len(self.tabuleiro)-1:
                        self.bt[i-1][j]["bg"]="blue"
                        self.bt[i-1][j]["state"]=DISABLED
                    elif i-1<0:
                        self.bt[i+1][j]["bg"]="blue"
                        self.bt[i+1][j]["state"]=DISABLED
                    elif i+1<=len(self.tabuleiro)-1 and i-1>=0:
                        self.bt[i+1][j]["bg"]="blue"
                        self.bt[i+1][j]["state"]=DISABLED
                        self.bt[i-1][j]["bg"]="blue"
                        self.bt[i-1][j]["state"]=DISABLED

                #Botões ao redor vertical
                if self.vertica_horizontal_5==1:
                    if i==navio_5_vertical [0]:
                        navio_vertical_0()
                    if i==navio_5_vertical [-1]:
                        navio_vertical_1()
                    if j+1>len(self.tabuleiro)-1:
                        self.bt[i][j-1]["bg"]="blue"
                        self.bt[i][j-1]["state"]=DISABLED
                    elif j-1<0:
                        self.bt[i][j+1]["bg"]="blue"
                        self.bt[i][j+1]["state"]=DISABLED
                    elif j+1<=len(self.tabuleiro)-1 and j-1>=0:
                        self.bt[i][j+1]["bg"]="blue"
                        self.bt[i][j+1]["state"]=DISABLED
                        self.bt[i][j-1]["bg"]="blue"
                        self.bt[i][j-1]["state"]=DISABLED
                        
                if self.navio_clicado_5==5:
                    self.bt_navio5["bg"]="#A9A9A9"
                    self.txt_navio5["fg"]="#A9A9A9"
                    
            if self.tabuleiro[i][j]=="B":
                winsound.PlaySound(tiro_bomba,winsound.SND_ASYNC)
                self.vida-=1
                self.bt[i][j]["bg"]="red"
                self.bt[i][j]["state"]=DISABLED
                self.txt_vidas["text"]="VIDAS: "+str(self.vida)
                self.txt_vidas["fg"]="red"
                
            self.navio_clicado=self.navio_clicado_1+self.navio_clicado_2+self.navio_clicado_3+self.navio_clicado_4+self.navio_clicado_5
            if self.qntd_navios==self.navio_clicado or self.vida==0:
                self.jan_final()

        #Criando botões que são navios
        self.bt[i][j] = Button(Janela, bg="#6495ED", activebackground="#6495ED",width=4, height=2, bd=2, command=clique_navio, state=NORMAL,cursor="target", relief=GROOVE)
        self.bt[i][j].place(x=posi_x, y=posi_y)

    def bt_agua(self, i, j,posi_x,posi_y):
        # Ação a ser realizada, quando o botão "x" for clicado
        def clique_agua():
            winsound.PlaySound(tiro_agua,winsound.SND_ASYNC)
            self.bt[i][j]["bg"] = "blue"
            self.bt[i][j]["state"] = DISABLED
            self.txt_vidas["fg"]="#008B8B"
        # Criando botões água
        self.bt[i][j] = Button(Janela, bg="#6495ED", width=4, height=2, bd=2, command=clique_agua, state=NORMAL, cursor="target", relief=GROOVE,activebackground="#6495ED")
        self.bt[i][j].place(x=posi_x, y=posi_y)

    #Janela do jogo
    def jan_jogo(self,nivel):
        winsound.PlaySound("Vazio",winsound.SND_PURGE)
        #Apagando widgets do inicio
        self.bt_facil.place_forget()
        self.bt_medio.place_forget()
        self.bt_dificil.place_forget()
        self.selecione.place_forget()
        self.como_jogar.place_forget()
        self.txt_como_jogar.place_forget()
        num_vertica_horizontal = [0, 1]
        
        def bomba():
            bomba = []
            posicao_coluna_aleatoria = random.choice(numeros)
            posicao_linha_aleatoria = random.choice(numeros)
            posicao_coluna_b = posicao_coluna_aleatoria
            posicao_linha_b = posicao_linha_aleatoria
            restricao_linha_b = []
            restricao_coluna_b = []
            while True:
                if self.tabuleiro[posicao_linha_b][posicao_coluna_b] == "x":
                    break
                if self.tabuleiro[posicao_linha_b][posicao_coluna_b] != "x":
                    posicao_coluna_b = random.choice(numeros)
                    posicao_linha_b = random.choice(numeros)
            for i in range((posicao_coluna_b - 1), (posicao_coluna_b + 2)):
                restricao_coluna_b.append(i)
            for i in range((posicao_linha_b - 1), (posicao_linha_b + 1)):
                restricao_linha_b.append(i)
            for i in range(posicao_coluna_b, posicao_coluna_b + 1):
                bomba.append(i)
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro)):
                    if i == posicao_linha_b:
                        if j in bomba:
                            self.tabuleiro[i][j] = 'B'

        def barco_1():
            navio_1_horizontal = []
            posicao_coluna_aleatoria = random.choice(numeros)
            posicao_linha_aleatoria = random.choice(numeros)
            posicao_coluna_1 = posicao_coluna_aleatoria
            posicao_linha_1 = posicao_linha_aleatoria
            restricao_linha_1 = []
            restricao_coluna_1 = []
            while True:  
                if (posicao_coluna_1) <= 9:
                    break
                if (posicao_coluna_1) > 9:
                    posicao_coluna_1 -= 1
            for i in range((posicao_coluna_1 - 1), (posicao_coluna_1 + 2)):
                restricao_coluna_1.append(i)
            for i in range((posicao_linha_1 - 1), (posicao_linha_1 + 2)):
                restricao_linha_1.append(i)
            for i in range(posicao_coluna_1, posicao_coluna_1 + 1):
                navio_1_horizontal.append(i)
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro)):
                    if i == posicao_linha_1:
                        if j in navio_1_horizontal:
                            self.tabuleiro[i][j] = '1'

                    if i == posicao_linha_1 - 1 or i == posicao_linha_1 + 1:
                        if j in restricao_coluna_1:
                            try:
                                self.tabuleiro[i][j] = '-'
                            except:
                                pass
                    if i == posicao_linha_1:
                        if j == posicao_coluna_1 - 1 or j == posicao_coluna_1 + 1:
                            try:
                                self.tabuleiro[i][j] = '|'
                            except:
                                pass

        def barco_2():
            global navio_2_horizontal,navio_2_vertical 
            restricoes_linhas = []
            restricoes_colunas = []
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if self.tabuleiro[i][j] == "1" or self.tabuleiro[i][j] == "|" or self.tabuleiro[i][j] == "-":
                        restricoes_linhas.append(i)
                        break
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if self.tabuleiro[i][j] == "1" or self.tabuleiro[i][j] == "|" or self.tabuleiro[i][j] == "-":
                        if j in restricoes_colunas:
                            pass
                        else:
                            restricoes_colunas.append(j)
                            
            navio_2_horizontal = []
            navio_2_vertical = []
            posicao_coluna_aleatoria = random.choice(numeros)
            posicao_linha_aleatoria = random.choice(numeros)
            posicao_coluna_2 = posicao_coluna_aleatoria
            posicao_linha_2 = posicao_linha_aleatoria
            self.vertica_horizontal_2 = random.choice(num_vertica_horizontal)
            restricao_linha_2 = []
            restricao_coluna_2 = []
            if self.vertica_horizontal_2 == 0:
                while True:
                    for i in range(posicao_coluna_2 - 1, posicao_coluna_2 + 2):
                        if i in restricoes_colunas:
                            posicao_coluna_2 = random.choice(numeros)
                    if not posicao_coluna_2 in restricoes_colunas:
                        break
                while True:
                    for i in range(posicao_linha_2 - 1, posicao_linha_2 + 2):
                        if i in restricoes_linhas:
                            posicao_linha_2 = random.choice(numeros)
                    if not posicao_linha_2 in restricoes_linhas:
                        break
                while True: 
                    if (posicao_coluna_2 + 1) <= 9:
                        break
                    if (posicao_coluna_2 + 1) > 9:
                        posicao_coluna_2 -= 1
                for i in range((posicao_linha_2 - 1), (posicao_linha_2 + 2)):
                    restricao_linha_2.append(i)
                for i in range((posicao_coluna_2 - 1), (posicao_coluna_2 + 3)):
                    restricao_coluna_2.append(i)
                for i in range(posicao_coluna_2, posicao_coluna_2 + 2):
                    navio_2_horizontal.append(i)
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro)):
                        if i == posicao_linha_2:
                            if j in navio_2_horizontal:
                                self.tabuleiro[i][j] = '2'

                        if i == posicao_linha_2 - 1 or i == posicao_linha_2 + 1:
                            if j in restricao_coluna_2:
                                try:
                                    self.tabuleiro[i][j] = '-'
                                except:
                                    pass
                        if i == posicao_linha_2:
                            if j == posicao_coluna_2 - 1 or j == posicao_coluna_2 + 2:
                                try:
                                    self.tabuleiro[i][j] = '|'
                                except:
                                    pass

            if self.vertica_horizontal_2 == 1:
                while True:
                    for i in range(posicao_coluna_2 - 1, posicao_coluna_2 + 2):
                        if i in restricoes_colunas:
                            posicao_coluna_2 = random.choice(numeros)
                    if not posicao_coluna_2 in restricoes_colunas:
                        break
                while True:
                    for i in range(posicao_linha_2 - 1, posicao_linha_2 + 2):
                        if i in restricoes_linhas:
                            posicao_linha_2 = random.choice(numeros)
                    if not posicao_linha_2 in restricoes_linhas:
                        break
                while True: 
                    if (posicao_linha_2 + 1) <= 9:
                        break
                    if (posicao_linha_2 + 1) > 9:
                        posicao_linha_2 -= 1
                for i in range((posicao_linha_2 - 1), (posicao_linha_2 + 3)):
                    restricao_linha_2.append(i)
                for i in range((posicao_coluna_2 - 1), (posicao_coluna_2 + 2)):
                    restricao_coluna_2.append(i)
                for i in range(posicao_linha_2, posicao_linha_2 + 2):
                    navio_2_vertical.append(i)
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro)):
                        if i in navio_2_vertical:
                            if j == posicao_coluna_2:
                                self.tabuleiro[i][j] = '2'
                        if j == posicao_coluna_2 - 1 or j == posicao_coluna_2 + 1:
                            if i in restricao_linha_2:
                                try:
                                    self.tabuleiro[i][j] = '|'
                                except:
                                    pass
                        if j == posicao_coluna_2:
                            if (i == posicao_linha_2 - 1) or (i == posicao_linha_2 + 2):
                                try:
                                    self.tabuleiro[i][j] = '-'
                                except:
                                    pass

        def barco_3():
            global navio_3_horizontal,navio_3_vertical
            restricoes_linhas = []
            restricoes_colunas = []
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if self.tabuleiro[i][j] == "1" or self.tabuleiro[i][j] == "2" or self.tabuleiro[i][j] == "|" or self.tabuleiro[i][j] == "-":
                        restricoes_linhas.append(i)
                        break
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if self.tabuleiro[i][j] == "1" or self.tabuleiro[i][j] == "2" or self.tabuleiro[i][j] == "|" or self.tabuleiro[i][j] == "-":
                        if j in restricoes_colunas:
                            pass
                        else:
                            restricoes_colunas.append(j)

            navio_3_horizontal = []
            navio_3_vertical = []
            posicao_coluna_aleatoria = random.choice(numeros)
            posicao_linha_aleatoria = random.choice(numeros)
            posicao_coluna_3 = posicao_coluna_aleatoria
            posicao_linha_3 = posicao_linha_aleatoria
            self.vertica_horizontal_3 = random.choice(num_vertica_horizontal)
            restricao_linha_3 = []
            restricao_coluna_3 = []
            if self.vertica_horizontal_3 == 0:
                while True:
                    for i in range(posicao_coluna_3 - 1, posicao_coluna_3 + 3):
                        if i in restricoes_colunas:
                            posicao_coluna_3 = random.choice(numeros)
                    if not posicao_coluna_3 in restricoes_colunas:
                        break
                while True:
                    for i in range(posicao_linha_3 - 1, posicao_linha_3 + 3):
                        if i in restricoes_linhas:
                            posicao_linha_3 = random.choice(numeros)
                    if not posicao_linha_3 in restricoes_linhas:
                        break
                while True: 
                    if (posicao_coluna_3 + 2) <= 9:
                        break
                    if (posicao_coluna_3 + 2) > 9:
                        posicao_coluna_3 -= 1
    
                for i in range((posicao_coluna_3 - 1), (posicao_coluna_3 + 4)):
                    restricao_coluna_3.append(i)
                for i in range((posicao_linha_3 - 1), (posicao_linha_3 + 2)):
                    restricao_linha_3.append(i)
                for i in range(posicao_coluna_3, posicao_coluna_3 + 3):
                    navio_3_horizontal.append(i)
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro)):
                        if i == posicao_linha_3:
                            if j in navio_3_horizontal:
                                self.tabuleiro[i][j] = '3'

                        if i == posicao_linha_3 - 1 or i == posicao_linha_3 + 1:
                            if j in restricao_coluna_3:
                                try:
                                    self.tabuleiro[i][j] = '-'
                                except:
                                    pass
                        if i == posicao_linha_3:
                            if j == posicao_coluna_3 - 1 or j == posicao_coluna_3 + 3:
                                try:
                                    self.tabuleiro[i][j] = '|'
                                except:
                                    pass

            if self.vertica_horizontal_3 == 1:
                while True:
                    for i in range(posicao_coluna_3 - 1, posicao_coluna_3 + 3):
                        if i in restricoes_colunas:
                            posicao_coluna_3 = random.choice(numeros)
                    if not posicao_coluna_3 in restricoes_colunas:
                        break
                while True:
                    for i in range(posicao_linha_3 - 1, posicao_linha_3 + 3):
                        if i in restricoes_linhas:
                            posicao_linha_3 = random.choice(numeros)
                    if not posicao_linha_3 in restricoes_linhas:
                        break
                while True: 
                    if (posicao_linha_3 + 2) <= 9:
                        break
                    if (posicao_linha_3 + 2) > 9:
                        posicao_linha_3 -= 1
                for i in range((posicao_linha_3 - 1), (posicao_linha_3 + 4)):
                    restricao_linha_3.append(i)
                for i in range((posicao_coluna_3 - 1), (posicao_coluna_3 + 2)):
                    restricao_coluna_3.append(i)
                for i in range(posicao_linha_3, posicao_linha_3 + 3):
                    navio_3_vertical.append(i)
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro)):
                        if i in navio_3_vertical:
                            if j == posicao_coluna_3:
                                self.tabuleiro[i][j] = '3'
                        if j == posicao_coluna_3 - 1 or j == posicao_coluna_3 + 1:
                            if i in restricao_linha_3:
                                try:
                                    self.tabuleiro[i][j] = '|'
                                except:
                                    pass
                        if j == posicao_coluna_3:
                            if (i == posicao_linha_3 - 1) or (i == posicao_linha_3 + 3):
                                try:
                                    self.tabuleiro[i][j] = '-'
                                except:
                                    pass

        def barco_4():
            global navio_4_horizontal,navio_4_vertical
            restricoes_linhas = []
            restricoes_colunas = []
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if self.tabuleiro[i][j] == "1" or self.tabuleiro[i][j] == "2" or  self.tabuleiro[i][j] == "3" or self.tabuleiro[i][j] == "|" or self.tabuleiro[i][j] == "-":
                        restricoes_linhas.append(i)
                        break
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if self.tabuleiro[i][j] == "1" or self.tabuleiro[i][j] == "2" or self.tabuleiro[i][j] == "3" or self.tabuleiro[i][j] == "|" or self.tabuleiro[i][j] == "-":
                        if j in restricoes_colunas:
                            pass
                        else:
                            restricoes_colunas.append(j)

            navio_4_horizontal = []
            navio_4_vertical = []
            posicao_coluna_aleatoria = random.choice(numeros)
            posicao_linha_aleatoria = random.choice(numeros)
            posicao_coluna_4 = posicao_coluna_aleatoria
            posicao_linha_4 = posicao_linha_aleatoria
            self.vertica_horizontal_4 = random.choice(num_vertica_horizontal)
            if self.vertica_horizontal_4 == 0:
                while True:
                    for i in range(posicao_coluna_4-1,posicao_coluna_4+4) :
                        if i in restricoes_colunas:
                            posicao_coluna_4 = random.choice(numeros)
                    if not posicao_coluna_4 in restricoes_colunas:
                        break
                while True:
                    for i in range(posicao_linha_4-1,posicao_linha_4+4) :
                        if i in restricoes_linhas:
                            posicao_linha_4 = random.choice(numeros)
                    if not posicao_linha_4 in restricoes_linhas:
                        break
                while True:  
                    if (posicao_coluna_4 + 3) <= 9:
                        break
                    if (posicao_coluna_4 + 3) > 9:
                        posicao_coluna_4 -= 1
                restricao = []
                for i in range((posicao_coluna_4 - 1), (posicao_coluna_4 + 5)):
                    restricao.append(i)
                for i in range(posicao_coluna_4, posicao_coluna_4 + 4):
                    navio_4_horizontal.append(i)
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro)):
                        if i == posicao_linha_4:
                            if j in navio_4_horizontal:
                                self.tabuleiro[i][j] = '4'

                        if i == posicao_linha_4 - 1 or i == posicao_linha_4 + 1:
                            if j in restricao:
                                try:
                                    self.tabuleiro[i][j] = '-'
                                except:
                                    pass
                        if i == posicao_linha_4:
                            if j == posicao_coluna_4 - 1 or j == posicao_coluna_4 + 4:
                                try:
                                    self.tabuleiro[i][j] = '|'
                                except:
                                    pass

            if self.vertica_horizontal_4 == 1:
                while True:
                    for i in range(posicao_coluna_4-1,posicao_coluna_4+4) :
                        if i in restricoes_colunas:
                            posicao_coluna_4 = random.choice(numeros)
                    if not posicao_coluna_4 in restricoes_colunas:
                        break
                while True:
                    for i in range(posicao_linha_4-1,posicao_linha_4+4) :
                        if i in restricoes_linhas:
                            posicao_linha_4 = random.choice(numeros)
                    if not posicao_linha_4 in restricoes_linhas:
                        break
                while True:  
                    if (posicao_linha_4 + 3) <= 9:
                        break
                    if (posicao_linha_4 + 3) > 9:
                        posicao_linha_4 -= 1
                restricao = []
                for i in range((posicao_linha_4 - 1), (posicao_linha_4 + 5)):
                    restricao.append(i)
                for i in range(posicao_linha_4, posicao_linha_4 + 4):
                    navio_4_vertical.append(i)
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro)):
                        if i in navio_4_vertical:
                            if j == posicao_coluna_4:
                                self.tabuleiro[i][j] = '4'

                        if j == posicao_coluna_4 - 1 or j == posicao_coluna_4 + 1:
                            if i in restricao:
                                try:
                                    self.tabuleiro[i][j] = '|'
                                except:
                                    pass
                        if j == posicao_coluna_4:
                            if (i == posicao_linha_4 - 1) or (i == posicao_linha_4 + 4):
                                try:
                                    self.tabuleiro[i][j] = '-'
                                except:
                                    pass

        def barco_5():
            global navio_5_horizontal,navio_5_vertical
            restricoes_linhas = []
            restricoes_colunas = []
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if self.tabuleiro[i][j] == "1" or self.tabuleiro[i][j] == "2" or self.tabuleiro[i][j] == "3" or self.tabuleiro[i][j] == "4" or self.tabuleiro[i][j] == "|" or self.tabuleiro[i][j] == "-":
                        restricoes_linhas.append(i)
                        break
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if self.tabuleiro[i][j] == "1" or self.tabuleiro[i][j] == "2" or self.tabuleiro[i][j] == "3" or self.tabuleiro[i][j] == "4" or self.tabuleiro[i][j] == "|" or self.tabuleiro[i][j] == "-":
                        if j in restricoes_colunas:
                            pass
                        else:
                            restricoes_colunas.append(j)
                            
            navio_5_horizontal = []
            navio_5_vertical = []
            posicao_coluna_aleatoria = random.choice(numeros)
            posicao_linha_aleatoria = random.choice(numeros)
            posicao_coluna_5 = posicao_coluna_aleatoria
            posicao_linha_5 = posicao_linha_aleatoria
            self.vertica_horizontal_5 = random.choice(num_vertica_horizontal)
            if self.vertica_horizontal_5 == 0:
                while True:
                    for i in range(posicao_coluna_5-1,posicao_coluna_5+5) :
                        if i in restricoes_colunas:
                            posicao_coluna_5 = random.choice(numeros)
                    if not posicao_coluna_5 in restricoes_colunas:
                        break
                while True:
                    for i in range(posicao_linha_5-1,posicao_linha_5+5) :
                        if i in restricoes_linhas:
                            posicao_linha_5 = random.choice(numeros)
                    if not posicao_linha_5 in restricoes_linhas:
                        break
                while True:   
                    if (posicao_coluna_5 + 4) <= 9:
                        break
                    if (posicao_coluna_5 + 4) > 9:
                        posicao_coluna_5 -= 1
                restricao = []
                for i in range((posicao_coluna_5 - 1) , (posicao_coluna_5 + 6)):
                    restricao.append(i)
                for i in range(posicao_coluna_5, posicao_coluna_5 + 5):
                    navio_5_horizontal.append(i)
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro)):
                        if i == posicao_linha_5:
                            if j in navio_5_horizontal:
                                self.tabuleiro[i][j] = '5'

                        if i == posicao_linha_5 - 1 or i == posicao_linha_5 + 1 :
                            if j in restricao:
                                try:
                                    self.tabuleiro[i][j] = '-'
                                except:
                                    pass
                        if i == posicao_linha_5:
                            if j == posicao_coluna_5 - 1 or j == posicao_coluna_5 + 5:
                                try:
                                    self.tabuleiro[i][j] = '|'
                                except:
                                    pass

            if self.vertica_horizontal_5 == 1:
                while True:
                    for i in range(posicao_coluna_5-1,posicao_coluna_5+5) :
                        if i in restricoes_colunas:
                            posicao_coluna_5 = random.choice(numeros)
                    if not posicao_coluna_5 in restricoes_colunas:
                        break
                while True:
                    for i in range(posicao_linha_5-1,posicao_linha_5+5) :
                        if i in restricoes_linhas:
                            posicao_linha_5 = random.choice(numeros)
                    if not posicao_linha_5 in restricoes_linhas:
                        break
                while True:   
                    if (posicao_linha_5 + 4) <= 9:
                        break
                    if (posicao_linha_5 + 4) > 9:
                        posicao_linha_5 -= 1
                restricao = []
                for i in range((posicao_linha_5 - 1) , (posicao_linha_5 + 6)):
                    restricao.append(i)
                for i in range(posicao_linha_5, posicao_linha_5 + 5):
                    navio_5_vertical.append(i)
                for i in range(len(self.tabuleiro)):
                    for j in range(len(self.tabuleiro)):
                        if i in navio_5_vertical:
                            if j == posicao_coluna_5:
                                self.tabuleiro[i][j] = '5'

                        if j == posicao_coluna_5 - 1 or j == posicao_coluna_5 + 1 :
                            if i in restricao:
                                try:
                                    self.tabuleiro[i][j] = '|'
                                except:
                                    pass
                        if j == posicao_coluna_5:
                            if (i == posicao_linha_5 - 1) or (i == posicao_linha_5 + 5):
                                try:
                                    self.tabuleiro[i][j] = '-'
                                except:
                                    pass

        def nv_facil():
            barco_1()
            barco_2()
            barco_3()
            for i in range(5):
                bomba()

        def nv_medio():
            barco_1()
            barco_2()
            barco_3()
            barco_4()
            for i in range(6):
                bomba()

        def nv_dificil():
            barco_1()
            barco_2()
            barco_3()
            barco_4()
            barco_5()
            for i in range(8):
                bomba()

        def legenda():
            if nivel==1:
                self.bt_bomba = Button(Janela, bg="red", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_bomba.place(x=420,y=36)
                self.txt_bomba=Label(Janela,text="BOMBA", fg="#008B8B", font=self.fontes[3])
                self.txt_bomba.place(x=465,y=46)
                self.bt_tiro_agua = Button(Janela, bg="blue", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_tiro_agua.place(x=420,y=86)
                self.txt_tiro_agua=Label(Janela,text="TIRO NA AGUA", fg="#008B8B", font=self.fontes[3])
                self.txt_tiro_agua.place(x=465,y=96)
                self.bt_navio1 = Button(Janela, bg="#FFD700", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio1.place(x=420,y=136)
                self.txt_navio1=Label(Janela,text="1 - BOIA", fg="#008B8B", font=self.fontes[3])
                self.txt_navio1.place(x=465,y=146)
                self.bt_navio2 = Button(Janela, bg="#228B22", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio2.place(x=420,y=186)
                self.txt_navio2=Label(Janela,text="2 - CORVETA", fg="#008B8B", font=self.fontes[3])
                self.txt_navio2.place(x=465,y=196)
                self.bt_navio3 = Button(Janela, bg="#FFA500", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio3.place(x=420,y=236)
                self.txt_navio3=Label(Janela,text="3 - SUBMARINO", fg="#008B8B", font=self.fontes[3])
                self.txt_navio3.place(x=465,y=246)
                self.txt_vidas=Label(Janela,text="VIDAS: "+str(self.vida), fg="#008B8B", font=self.fontes[1])
                self.txt_vidas.place(x=450,y=340)
                self.bt_desistir = Button(Janela, text="DESISTIR" ,fg="#008B8B", activeforeground="#008B8B", relief=FLAT,font=self.fontes[1],command=self.fechar)
                self.bt_desistir.place(x=445,y=376)
            if nivel==2:
                self.bt_bomba = Button(Janela, bg="red", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_bomba.place(x=490,y=36)
                self.txt_bomba=Label(Janela,text="BOMBA", fg="#008B8B", font=self.fontes[3])
                self.txt_bomba.place(x=535,y=46)
                self.bt_tiro_agua = Button(Janela, bg="blue", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_tiro_agua.place(x=490,y=86)
                self.txt_tiro_agua=Label(Janela,text="TIRO NA AGUA", fg="#008B8B", font=self.fontes[3])
                self.txt_tiro_agua.place(x=535,y=96)
                self.bt_navio1 = Button(Janela, bg="#FFD700", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio1.place(x=490,y=136)
                self.txt_navio1=Label(Janela,text="1 - BOIA", fg="#008B8B", font=self.fontes[3])
                self.txt_navio1.place(x=535,y=146)
                self.bt_navio2 = Button(Janela, bg="#228B22", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio2.place(x=490,y=186)
                self.txt_navio2=Label(Janela,text="2 - CORVETA", fg="#008B8B", font=self.fontes[3])
                self.txt_navio2.place(x=535,y=196)
                self.bt_navio3 = Button(Janela, bg="#FFA500", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio3.place(x=490,y=236)
                self.txt_navio3=Label(Janela,text="3 - SUBMARINO", fg="#008B8B", font=self.fontes[3])
                self.txt_navio3.place(x=535,y=246)
                self.bt_navio4 = Button(Janela, bg="#9400D3", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio4.place(x=490,y=286)
                self.txt_navio4=Label(Janela,text="4 - DESTROYER", fg="#008B8B", font=self.fontes[3])
                self.txt_navio4.place(x=535,y=296)
                self.txt_vidas=Label(Janela,text="VIDAS: "+str(self.vida), fg="#008B8B", font=self.fontes[1])
                self.txt_vidas.place(x=520,y=424)
                self.bt_desistir = Button(Janela, text="DESISTIR" ,fg="#008B8B", activeforeground="#008B8B", relief=FLAT,font=self.fontes[1],command=self.fechar)
                self.bt_desistir.place(x=515,y=460)
            if nivel==3:
                self.bt_bomba = Button(Janela, bg="red", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_bomba.place(x=630,y=36)
                self.txt_bomba=Label(Janela,text="BOMBA", fg="#008B8B", font=self.fontes[3])
                self.txt_bomba.place(x=675,y=46)
                self.bt_tiro_agua = Button(Janela, bg="blue", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_tiro_agua.place(x=630,y=86)
                self.txt_tiro_agua=Label(Janela,text="TIRO NA AGUA", fg="#008B8B", font=self.fontes[3])
                self.txt_tiro_agua.place(x=675,y=96)
                self.bt_navio1 = Button(Janela, bg="#FFD700", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio1.place(x=630,y=136)
                self.txt_navio1=Label(Janela,text="1 - BOIA", fg="#008B8B", font=self.fontes[3])
                self.txt_navio1.place(x=675,y=146)
                self.bt_navio2 = Button(Janela, bg="#228B22", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio2.place(x=630,y=186)
                self.txt_navio2=Label(Janela,text="2 - CORVETA", fg="#008B8B", font=self.fontes[3])
                self.txt_navio2.place(x=675,y=196)
                self.bt_navio3 = Button(Janela, bg="#FFA500", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio3.place(x=630,y=236)
                self.txt_navio3=Label(Janela,text="3 - SUBMARINO", fg="#008B8B", font=self.fontes[3])
                self.txt_navio3.place(x=675,y=246)
                self.bt_navio4 = Button(Janela, bg="#9400D3", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio4.place(x=630,y=286)
                self.txt_navio4=Label(Janela,text="4 - DESTROYER", fg="#008B8B", font=self.fontes[3])
                self.txt_navio4.place(x=675,y=296)
                self.bt_navio5 = Button(Janela, bg="#2F4F4F", width=4, height=2, bd=2, state=DISABLED, relief=GROOVE)
                self.bt_navio5.place(x=630,y=336)
                self.txt_navio5=Label(Janela,text="5 - PORTA-AVIOES", fg="#008B8B", font=self.fontes[3])
                self.txt_navio5.place(x=675,y=346)
                self.txt_vidas=Label(Janela,text="VIDAS: "+str(self.vida), fg="#008B8B", font=self.fontes[1])
                self.txt_vidas.place(x=685,y=570)
                self.bt_desistir = Button(Janela, text="DESISTIR" ,fg="#008B8B", activeforeground="#008B8B", relief=FLAT,font=self.fontes[1],command=self.fechar)
                self.bt_desistir.place(x=680,y=600)   
                

                
        # Função para contar quantos barcos tem no tabuleiro
        def conta_barcos():
            self.qntd_navios=0
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if self.tabuleiro[i][j] == "1" or self.tabuleiro[i][j] == "2" or self.tabuleiro[i][j] == "3" or self.tabuleiro[i][j] == "4" or self.tabuleiro[i][j] == "5":
                        self.qntd_navios+=1

        if (nivel==1):
            numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            Janela.geometry('605x450+400+150')
            self.tabuleiro = []

            for i in range(10):
                self.tabuleiro.append(["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"])

            nv_facil()

            # Construção do tabuleiro10x10 na interface
            letras = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K"]
            numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            #Criando uma matriz para substituir por botões
            self.bt = []
            self.lista_letras=[]
            self.lista_numeros=[]
            for i in range(10):
                self.lista_numeros.append("x")
                self.lista_letras.append("x")
                self.bt.append([])
                for j in range(10):
                    self.bt[i].append("x")

            posi_x=0
            posi_y=36
            #Criando os botões
            for i in range(10):
                if i>=1:
                    posi_y+=39
                self.lista_letras[i]=Label(Janela, text=letras[i], fg="#008B8B", font=self.fontes[1])
                self.lista_letras[i].place(x=2, y=posi_y)
                for j in range(10):
                    posi_x+=36
                    if i == 0:
                        self.lista_numeros[j]=Label(Janela, text=numeros[j], fg="#008B8B", font=self.fontes[1])
                        self.lista_numeros[j].place(x=posi_x + 2, y=0)
                    if self.tabuleiro[i][j]== "1" or self.tabuleiro[i][j]== "2" or self.tabuleiro[i][j]== "3" or self.tabuleiro[i][j]== "B":
                        self.bt_navio(i, j,posi_x,posi_y)
                    if self.tabuleiro[i][j] == "x" or self.tabuleiro[i][j] == "-" or self.tabuleiro[i][j] == "|":
                        self.bt_agua(i, j,posi_x,posi_y)
                posi_x=0
            
            legenda()
            conta_barcos()

        elif (nivel==2):
            numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            Janela.geometry('690x520+340+100')
            self.tabuleiro = []

            for i in range(12):
                self.tabuleiro.append(["x", "x", "x", "x", "x", "x", "x", "x", "x", "x","x", "x"])

            nv_medio()

            # Construção do tabuleiro10x10 na interface
            letras = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M"]
            numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11","12"]
            #Criando uma matriz para substituir por botões
            self.bt = []
            self.lista_letras=[]
            self.lista_numeros=[]
            for i in range(12):
                self.lista_numeros.append("x")
                self.lista_letras.append("x")
                self.bt.append([])
                for j in range(12):
                    self.bt[i].append("x")

            posi_x=0
            posi_y=36
            #Criando os botões
            for i in range(12):
                if i>=1:
                    posi_y+=39
                self.lista_letras[i]=Label(Janela, text=letras[i], fg="#008B8B", font=self.fontes[1])
                self.lista_letras[i].place(x=2, y=posi_y)
                for j in range(12):
                    posi_x+=36
                    if i == 0:
                        self.lista_numeros[j]=Label(Janela, text=numeros[j], fg="#008B8B", font=self.fontes[1])
                        self.lista_numeros[j].place(x=posi_x + 2, y=0)
                    if self.tabuleiro[i][j]== "1" or self.tabuleiro[i][j]== "2" or self.tabuleiro[i][j]== "3" or self.tabuleiro[i][j]== "4" or self.tabuleiro[i][j]== "B":
                        self.bt_navio(i, j,posi_x,posi_y)
                    if self.tabuleiro[i][j] == "x" or self.tabuleiro[i][j] == "-" or self.tabuleiro[i][j] == "|":
                        self.bt_agua(i, j,posi_x,posi_y)
                posi_x=0

            legenda()
            conta_barcos()

        elif (nivel==3):
            numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15]
            Janela.geometry('830x670+250+10')
            self.tabuleiro = []

            for i in range(16):
                self.tabuleiro.append(["x", "x", "x", "x", "x", "x", "x", "x", "x", "x","x", "x","x", "x","x","x"])

            nv_dificil()

            # Construção do tabuleiro10x10 na interface
            letras = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M","N","O","P","Q"]
            numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11","12","13","14","15","16"]
            #Criando uma matriz para substituir por botões
            self.bt = []
            self.lista_letras=[]
            self.lista_numeros=[]
            for i in range(16):
                self.lista_numeros.append("x")
                self.lista_letras.append("x")
                self.bt.append([])
                for j in range(16):
                    self.bt[i].append("x")

            posi_x=0
            posi_y=36
            #Criando os botões
            for i in range(16):
                if i>=1:
                    posi_y+=39
                self.lista_letras[i]=Label(Janela, text=letras[i], fg="#008B8B", font=self.fontes[1])
                self.lista_letras[i].place(x=2, y=posi_y)
                for j in range(16):
                    posi_x+=36
                    if i == 0:
                        self.lista_numeros[j]=Label(Janela, text=numeros[j], fg="#008B8B", font=self.fontes[1])
                        self.lista_numeros[j].place(x=posi_x + 2, y=0)
                    if self.tabuleiro[i][j]== "1" or self.tabuleiro[i][j]== "2" or self.tabuleiro[i][j]== "3" or self.tabuleiro[i][j]== "4" or self.tabuleiro[i][j]== "5" or self.tabuleiro[i][j]== "B":
                        self.bt_navio(i, j,posi_x,posi_y)
                    if self.tabuleiro[i][j] == "x" or self.tabuleiro[i][j] == "-" or self.tabuleiro[i][j] == "|":
                        self.bt_agua(i, j,posi_x,posi_y)
                posi_x=0

            legenda()
            conta_barcos()
            
        
    def jan_final(self):
        Janela.geometry('325x200+500+250')
        #Apagar numeros e letras
        for i in range(len(self.tabuleiro)):
            self.lista_numeros[i].place_forget()
            self.lista_letras[i].place_forget()
            for j in range(len(self.tabuleiro)):
                self.bt[i][j].place_forget()
        #Apagando legenda
        try:
            self.bt_bomba.place_forget()
            self.txt_bomba.place_forget()           
            self.bt_tiro_agua.place_forget()           
            self.txt_tiro_agua.place_forget()        
            self.bt_navio1.place_forget()       
            self.txt_navio1.place_forget()
            self.bt_navio2.place_forget()
            self.txt_navio2.place_forget()
            self.bt_navio3.place_forget()
            self.txt_navio3.place_forget()
            self.txt_vidas.place_forget()
            self.bt_desistir.place_forget()
            self.bt_navio4.place_forget()
            self.txt_navio4.place_forget()  
            self.bt_navio5.place_forget() 
            self.txt_navio5.place_forget()       
        except:
            pass
                    
        if self.qntd_navios==self.navio_clicado:
            self.txt_jan_final=Label(Janela,text="PARABENS, VOCE CONSEGUIU ACERTAR\nTODOS OS BARCOS!", fg="#008B8B", font=self.fontes[3])
            self.txt_jan_final.place(x=20,y=10)
        if self.vida==0:
            self.txt_jan_final=Label(Janela,text="VOCE PERDEU TODAS AS VIDAS,\nTENTE NOVAMENTE!", fg="#008B8B", font=font.Font(family="Fluo Gums", size=7))
            self.txt_jan_final.place(x=50,y=10)
        self.bt_jogar_novamente=Button(Janela,text="JOGAR NOVAMENTE",fg="#008B8B",activeforeground="#008B8B", command=self.dificuldade, font=self.fontes[3], relief=FLAT)
        self.bt_jogar_novamente.place(x=25,y=150)
        self.bt_sair = Button(Janela, text="SAIR", fg="#008B8B", activeforeground="#008B8B", command=self.fechar,font=self.fontes[3], relief=FLAT)
        self.bt_sair.place(x=250, y=150)
        self.voltar+=1

Janela = Tk()
Batalha_Naval(Janela)
winsound.PlaySound("Janela_inicial",winsound.SND_ASYNC|winsound.SND_LOOP)
Janela.title('Batalha Naval')
Janela.geometry('500x400+450+150')
Janela.wm_iconbitmap('icon.ico')
Janela.resizable(False,False)
Janela.mainloop()
