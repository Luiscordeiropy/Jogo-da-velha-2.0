from tkinter import *

# CORES -----------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co8 = "#3297a8"  # azul / blue
co7 = "#e85151"  # vermelho / red
co11 = "#a7dde6"  # azul claro
co12 = "#f19595"  # vermelho claro
fundo = "#3b3b3b"  # preta / black
# LOGICA DO JOGO---------------------------------------------------------------
prox_jogador = 0
jogando = "x"


def iniciar_jogo():
    global lista_click
    global contador
    global jogando
    ordem_jogada = []
    lista_click = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    contador = 0
    botao_iniciar["text"] = ""
    jogando = "x" if prox_jogador == 0 else "o"

    def controlar(i):
        global jogando
        global contador
        if lista_botoes[i]["text"] == "":
            # coloca a cor do texto de acordo com a cor do valor "X" ou "o"
            cor = co7 if jogando == "x" else co8
            lista_botoes[i]["fg"] = cor
            lista_botoes[i]["text"] = jogando
            # Aqui é determinado qual simbolo ficará semiapagado, ou seja, será a proxima a ser apagada
            cor_apagada()
            # determina a ordem correta das primeiras jogadas e apaga de acordo com a quantidade de jogadas
            apagar_jogada()
            # substitui um valor especifico da lista_click por "x" ou "o"
            substituir_click(i, 0) if i <= 2 else substituir_click(i, 1) \
                if i < 6 else substituir_click(i, 2)
            contador += 1
            # tem as possilidades de vitoria
            possibilidades()
            # faz a troca dos jogadores do "X" para o "o"
            jogando = "o" if jogando == "x" else "x"

    # obtém-se as possibilidades de vitória
    def possibilidades():
        global lista_click

        if contador >= 5:
            # horizontais
            any(vencedor("O vencedor foi", jogando) for i in range(1) for j in range(3) if
                lista_click[j][i] == lista_click[j][1+i] == lista_click[j][2+i])

            # verticais
            any(vencedor("O vencedor foi", jogando)for i in range(3) for j in range(1) if
                lista_click[j][i] == lista_click[1+j][i] == lista_click[2+j][i])

            # diagonais
            if lista_click[0][0] == lista_click[1][1] == lista_click[2][2]:
                vencedor("o vencedor foi ", jogando)
            if lista_click[0][2] == lista_click[1][1] == lista_click[2][0]:
                vencedor("o vencedor foi ", jogando)
    # determina quem irá receber o ponto e reiniciar o sistema 
    def vencedor(x=0, y=0):
        global lista_click
        global contador
        global ordem_jogada
        global prox_jogador
        print(f" {x} {y} ")
        botao_iniciar = Button(frame_baixo, command=iniciar_jogo, text="jogar novamente", height=2, width=14, bg=fundo,
                               fg=co0, font="Ivy 15 bold", relief="flat")
        botao_iniciar.place(x=128, y=320)
        
        if jogando == "x":
            ponto_x["text"] += 1
            prox_jogador = 1

        elif jogando == "o":
            ponto_o["text"] += 1
            prox_jogador = 0

        lista_click = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        contador = 0
        ordem_jogada = []
    # determina qual jogada irá ficar semiapagada 
    def cor_apagada():
        if contador == 5:
            t = ordem_jogada[0][0]
            lista_botoes[t]["fg"] = co12 if lista_botoes[t]["text"] == "x" else co11

        if contador >= 6:
            t = ordem_jogada[1][0]
            lista_botoes[t]["fg"] = co12 if lista_botoes[t]["text"] == "x" else co11
    # determina de acordo com a ordem qual simbolo será apagado
    def apagar_jogada():
        if contador >= 6:
            for (b, j, n) in ordem_jogada:
                lista_botoes[b]["text"] = ""
                lista_click[j][n] = b
                ordem_jogada.pop(0)
                break
    # substitui um valor da lista_click para o original
    def substituir_click(i, n):
        lista = i, n, lista_click[n].index(i)
        ordem_jogada.append(lista)
        lista_click[n].insert(lista_click[n].index(i), jogando)
        lista_click[n].remove(i)

    # CONFIGURANDO O FRAME DE BAIXO ----------------------------------------------------------
    def frame_de_baixo(texto, fonte, bg, height, width, x, y):
        linha = Label(frame_baixo, text=texto, font=fonte, bg=bg, height=height, width=width)
        linha.place(x=x, y=y)

    # LINHAS VERTICAIS
    frame_de_baixo("", "Ivy 10 bold", co0, 22, 1, 148, 12)
    frame_de_baixo("", "Ivy 10 bold", co0, 22, 1, 269, 12)

    # LINHAS HORIZONTAIS
    frame_de_baixo("", "Ivy 6 bold", co0, 1, 68, 42, 120)
    frame_de_baixo("", "Ivy 6 bold", co0, 1, 68, 42, 245)
    # botões
    lista_botoes = []
    posicoes = [(42, 12), (163, 12), (282, 12),  # LINHA 1
                (42, 137), (163, 137), (282, 137),  # LINHA 2
                (42, 262), (163, 262), (282, 262)]  # LINHA 3

    # Criação dos botões usando um loop
    for e, (x, y) in enumerate(posicoes, start=1):
        botao = Button(frame_baixo, command=lambda num=e - 1: controlar(num), text="", height=1, width=3, bg=fundo,
                       fg=co7, font="Ivy 40 bold", overrelief=RIDGE, relief="flat")
        botao.place(x=x, y=y)
        lista_botoes.append(botao)


# JANELA PRINCIPAL

janela = Tk()
janela.title('JOGO DO NOVO')
janela.geometry('450x600')
janela.configure(bg=fundo)

# DIVIDINDO A JANELA EM 2 -----------------------------------------------------------

frame_cima = Frame(janela, width=430, height=150, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=430, height=400, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW, padx=10, pady=10)


# CONFIGURANDO O FRAME DE CIMA -----------------------------------------------------


def frame_de_cima(texto, fonte, bg, fg, x, y):
    jogador = Label(frame_cima, text=texto, font=fonte, bg=bg, fg=fg)
    jogador.place(x=x, y=y)


frame_de_cima("X", "Ivy 60 bold", co1, co7, 70, 20)
frame_de_cima("Jogador 1", "ivy 10 bold", co1, co0, 65, 100)

frame_de_cima(":", "Ivy 55 bold", co1, co0, 190, 20)

frame_de_cima("o", "Ivy 80 bold", co1, co8, 280, -7)
frame_de_cima("Jogador 2", "ivy 10 bold", co1, co0, 280, 100)

# pontos do jogadores que vão ser modificados de acordo com a vitória
ponto_x = Label(frame_cima, text=0, font="Ivy 55 bold", bg=co1, fg=co0)
ponto_x.place(x=145, y=25)
ponto_o = Label(frame_cima, text=0, font="Ivy 55 bold", bg=co1, fg=co0)
ponto_o.place(x=220, y=25)

botao_iniciar = Button(frame_baixo, command=iniciar_jogo, text="JOGAR", height=2, width=11, bg=fundo, fg=co0,
                       font="Ivy 15 bold")
botao_iniciar.place(x=145, y=300)
janela.mainloop()
