 # -*- coding: latin-1 -*-

import pygame, sys
from pygame.locals import *
from random import *
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pylab
import re

FPS = 10
limite= 50
WINDOWWIDTH = 900
WINDOWHEIGHT = 800

BLACK = (0,  0,  0)
WHITE = (255,255,255)
DARKGRAY = (75, 75, 75)
DARK = (50, 50, 50)
BLUE = (150,   150, 255)
RED = (255, 0, 0)

def read_datafile(file_name):
    data = np.loadtxt(file_name, delimiter=';')
    return data

def real_time(i):
    an = i/185
    ms = 12*(i-an*185)/185
    anos = str(an)
    meses = str(ms)

    if an == 0:
        a = anos = ''
    elif an == 1:
        a = ' ano '
    else:
        a = ' anos '

    if ms == 0:
        m = meses = ''
    elif ms == 1:
        m = ' mês '
    else:
        m = ' meses '

    if an != 0 and ms != 0:
        e='e '
    else:
        e=''

    TR = "Tempo: "+anos+a+e+meses+m

    return TR


def timeExecution():
    contador = time.time() - ini
    #print contador
    horas = int(contador/3600)
    contador = contador - (3600 * horas)
    minutos = int(contador / 60)
    contador = contador - (60 * minutos)
    segundos = int(contador)
    horas = str(horas)
    minutos = str(minutos)
    segundos = str(segundos)
    s = re.sub(r'(^.$)', r'0\1',segundos)
    m = re.sub(r'(^.$)', r'0\1',minutos)
    h = re.sub(r'(^.$)', r'0\1',horas)
    relogio = 'Relógio: '+h+':'+m+':'+s
    contador=text.render(relogio,0,WHITE)
    DISPLAYSURF.blit(contador,(WINDOWWIDTH+25,10))


def colourGrid(item, lifeDict):
    x = item[0]
    y = item[1]
    y = y * CELLSIZE
    x = x * CELLSIZE
    if lifeDict[item] == 0:
        pygame.draw.rect(DISPLAYSURF, BLUE, (x, y, CELLSIZE*PIXELSIZE, CELLSIZE*PIXELSIZE))
    if lifeDict[item] == 1:
        pygame.draw.rect(DISPLAYSURF, RED, (x, y, CELLSIZE*PIXELSIZE, CELLSIZE*PIXELSIZE))

    return None


def riverGrid():
    gridDict = {}
    for y in range (CELLHEIGHT):
        for x in range (CELLWIDTH):
            gridDict[x,y] = int(A[y][x])
    return gridDict

def direct():
    beta = 3500

    for L in range(2, n-1):
            for C in range(2, m-1):
                A[L][C] = MA[L][C]

    for L in range(2, n-1):
        for C in range(2, m-1):
            if A[L][C] == 0:

                if A[L-1][C-1]==1:
                    v1=1
                else:
                    v1=0

                if A[L-1][C]==1:
                    v2=1
                else:
                    v2=0

                if A[L-1][C+1]==1:
                    v3=1
                else:
                    v3=0

                if A[L][C-1]==1:
                    v4=1
                else:
                    v4=0

                if A[L][C+1]==1:
                    v5=1
                else:
                    v5=0

                if A[L+1][C-1]==1:
                    v6=1
                else:
                    v6=0

                if A[L+1][C]==1:
                    v7=1
                else:
                    v7=0

                if A[L+1][C+1]==1:
                    v8=1
                else:
                    v8=0

                v =v1+v2+v3+v4+v5+v6+v7+v8
                pi = beta*v
                rio = random()
                if A[L][C] == 0 and rio*v > 0.01:
                    MA[L][C] = 1

                Pnl = random()
                Ro = 3.142
                D = random()*50

                if MA[L][C] == 1:
                    p1 = Pnl
                    p2 = random()
                    if p1 >= p2:
                        if random() > 0.1:
                            Ldir = 1
                        else:
                            Ldir = -1
                        if random() > 0.1:
                            Cdir = 1
                        else:
                            Cdir = -1

                        DL = D * Ldir + L
                        DC = D * Cdir + C

                        if DL < 1:
                            DL = 1
                        if DC < 1:
                            DC = 1
                        if DL > n - 1:
                            DL = n - 1
                        if DC > m - 1:
                            DC = m - 1

                        if A[DL][DC] == 0:
                            MA[DL][DC] = 1
    return MA


def main():
    i = 0
    pause = False
    Pause = text.render("Pause", True, WHITE)
    Start = text.render("Start", True, WHITE)

    if execucao > 4:
        fig = pylab.figure(figsize=[4, 4],dpi=50,)
        plt.boxplot(dados)
        plt.savefig('plot.png')
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pygame.image.fromstring(raw_data, size, "RGB")

    while MA[y][x] == 0:

        DISPLAYSURF.fill(DARKGRAY)
        DISPLAYSURF.blit(imagem,(0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if pause == False:
            i = i + 1
            Dict = direct()

        Stop = text.render("Sair", True, WHITE)
        StopRect = Stop.get_rect().move(WINDOWWIDTH+25,350)
        PauseRect = Pause.get_rect().move(WINDOWWIDTH+100,350)
        StartRect = Start.get_rect().move(WINDOWWIDTH+200,350)

        if StopRect.collidepoint(pygame.mouse.get_pos()) and comecou==True:
            Stop = text.render("Sair", True, (255,0,0))
            if pygame.mouse.get_pressed()[0]:
                return False

        if PauseRect.collidepoint(pygame.mouse.get_pos()) and comecou==True:
                if pygame.mouse.get_pressed()[0]:
                    pause = True

        if StartRect.collidepoint(pygame.mouse.get_pos()) and comecou==True:
                if pygame.mouse.get_pressed()[0]:
                    pause = False

        TempoReal = text.render(real_time(i), 0, WHITE)

        if execucao > limite:
            m1 = 0
            for i in range(limite):
                m1 = m1 + i
            media = m1/limite
            TempoReal = text.render(real_time(media), 0, WHITE)
            pause = True

        if (i - 1) % 2 == 0:

            lifeDict = riverGrid()
            for item in lifeDict:
                colourGrid(item, lifeDict)


            It = "Iterações :"+str(i)
            Ex = "Execução "+str(execucao)
            Iteracoes = text.render(It, 0, WHITE)
            Execucoes = text.render(Ex, 0, WHITE)

            DISPLAYSURF.blit(Execucoes,(WINDOWWIDTH+25,10))
            #DISPLAYSURF.blit(Iteracoes,(WINDOWWIDTH+25,100))
            DISPLAYSURF.blit(TempoReal,(WINDOWWIDTH+25,50))
            DISPLAYSURF.blit(Stop,(WINDOWWIDTH+25,350))
            DISPLAYSURF.blit(Pause,(WINDOWWIDTH+100,350))
            DISPLAYSURF.blit(Start,(WINDOWWIDTH+200,350))
            #timeExecution()

            if execucao > 4:
                DISPLAYSURF.blit(surf, (WINDOWWIDTH+25,100))
            pygame.display.update()

    dados.append(i)
    print execucao,":",dados

    return True

if __name__=='__main__':

    pygame.init()
    global DISPLAYSURF

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH+100,WINDOWHEIGHT))
    pygame.display.set_caption('Game of Limnoperna fortunei')
    text = pygame.font.SysFont("Arial", 30, False, True)

    comecou = False
    reloj = pygame.time.Clock()

    continuar = True
    while(continuar):
        reloj.tick(60)

        if comecou==False:

            logo = pygame.image.load("logoCBEIH.png")

            Nariz = text.render("Nariz de Minas", True, (0,0,0))
            NarizRect = Nariz.get_rect().move(100,150)

            Prata = text.render("Rio da Prata", True, (0,0,0))
            PrataRect = Prata.get_rect().move(100,200)

            PAfonso = text.render("Paulo Afonso", True, (0,0,0))
            PAfonsoRect = PAfonso.get_rect().move(100,250)

        for event in pygame.event.get():
            if event.type==QUIT:
                continuar = False

            dados = []
            while comecou == True:
                execucao = execucao + 1
                A =  read_datafile(B)
                MA = read_datafile(B)
                comecou = main()

        if PrataRect.collidepoint(pygame.mouse.get_pos()) and comecou==False:
            Prata = text.render("Rio da Prata", True, (255,0,0))
            if pygame.mouse.get_pressed()[0]:

                B = 'prata_fim.csv'
                imagem = pygame.image.load("Mapa_prata_assuncao.jpg")
                comecou = True
                CELLSIZE = 0.5
                PIXELSIZE = 4/CELLSIZE
                y=119
                x=519

        if PAfonsoRect.collidepoint(pygame.mouse.get_pos()) and comecou==False:
            PAfonso = text.render("Paulo Afonso", True, (255,0,0))
            if pygame.mouse.get_pressed()[0]:

                B = 'Sobradinho_pa.csv'
                imagem = pygame.image.load("sobradinho_PauloAfonso.png")
                comecou = True
                CELLSIZE = 1
                PIXELSIZE = 4/CELLSIZE
                y=250
                x=502

        if NarizRect.collidepoint(pygame.mouse.get_pos()) and comecou==False:
            Nariz = text.render("Nariz de Minas", True, (255,0,0))
            if pygame.mouse.get_pressed()[0]:

                B = 'nariz_minas.csv'
                imagem = pygame.image.load("mapa_parana_contorno.png")
                comecou = True
                CELLSIZE = 2
                PIXELSIZE = 4/CELLSIZE
                y=2
                x=4


        if comecou == True:
            MB = read_datafile(B)
            Dmax = MB.size
            m = MB[1].size
            n = Dmax/m
            CELLWIDTH = m
            CELLHEIGHT = n
            WINDOWWIDTH = m*CELLSIZE
            WINDOWHEIGHT = n*CELLSIZE

            execucao = 0
            ini = time.time()

        DISPLAYSURF.fill((255,255,255))
        DISPLAYSURF.blit(logo,(100,20))
        DISPLAYSURF.blit(Nariz,(100,150))
        DISPLAYSURF.blit(Prata,(100,200))
        DISPLAYSURF.blit(PAfonso,(100,250))

        pygame.display.flip()

# References:
#
# http://trevorappleton.blogspot.com.br/2013/07/python-game-of-life.html
# Melotti, G. 2009. Aplicação de Autômatos Celulares em Sistemas Complexos: Um Estudo de Caso em Espalhamento de Epidemias. Thesis, Universidade Federal de Minas Gerais.
