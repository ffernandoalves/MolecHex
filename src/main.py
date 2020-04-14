'''
Author: \251 ffernandoalves
Date: 03/2020
'''

import sys
import pygame
import os

from _start import Start
from _tools import Tools

#try:
#    pygame.init()
#except:
#    pass

#IMAGENS
#standard size: (40, 40)
path = ""
organism_img = pygame.image.load(os.path.join(path, 'player.jpg'))

#COLORS
#*particles colors
dic_color = [
    ('GREEN', (129,197,141), 0),
    ('PINK', (197, 131, 129), 1),
    ('BLUE', (155, 209, 205), 2),
    ('YELLOW', (204,187,153), 3),
    ('LIGHT_PURPLE', (209,135,201), 4),
    ('SWEET_BROWN', (168,65,64), 5), #púrpura
    ('KABUL', (106, 75,62), 6),      #marromTolete
    ('PURPLE', (183,157,217), 7)]    #roxo
#------------

#*environment colors
env_color = [
    ('GREY', (79,79,79), 0),
    ('WHITE', (255,255,255), 1),
    ('BLACK', (0,0,0), 2),
    ('RED', (255,0,0), 3),
    ('SILVER', (192,192,192), 4),
    ('ORANGE', (255,69,0), 5),
    ('LIGHT_GREY', (220,220,220), 6)]

'''def color_particle(n=11):
    #import random
    list_colors = []
    for i in range(0, n):
        pos_x = random.choice(range(0, 255))
        pos_y = random.choice(range(0, 255))
        pos_z = random.choice(range(0, 255))
        tupla_ = (pos_x, pos_y, pos_z)
        list_colors.append(tupla_)
    return list_colors'''
#------------

#SCREEN
CLOCK = pygame.time.Clock()
#BACKGROUND_COLOR = env_color[1][1]
BACKGROUND_COLOR = dic_color[2][1]
#padrao: WIDTH = 900; HEIGHT = 800
WIDTH = 900
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Particle Test')
#-----
BOTTON_BAR = 40
#Organism size
TAMANHO = 20

def main():
    start = Start(env_color, dic_color, SCREEN, size_matriz=11,
    organism_img=(False, organism_img, (40, 40)), hexagonal_shape=True,
    complete_matrix=False,
    matrix_shape=[None, #'rectangular' / 'square'
                (13, 16)])
    bar_tool = Tools(env_color, dic_color, WIDTH, HEIGHT, SCREEN)

    while start.executando:
            
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start.executando = False
                break

            if event.type == pygame.KEYUP:
                start.organismo.direcao = "parado"
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        start.organismo.direcao = "esquerda"
                if event.key == pygame.K_RIGHT:
                        start.organismo.direcao = "direita"
                if event.key == pygame.K_UP:
                        start.organismo.direcao = "cima"
                if event.key == pygame.K_DOWN:
                        start.organismo.direcao = "baixo"
            
        if start.executando:
            SCREEN.fill(BACKGROUND_COLOR)
            bar_tool.mouse_x, bar_tool.mouse_y = pygame.mouse.get_pos()
            bar_tool.pos_x, bar_tool.pos_y = start.organismo.x, start.organismo.y
            bar_tool.direcao()
            bar_tool.Cursor()
            #bar_tool.menu_moleculas()
            #bar_tool.matrix_original()
            start.gerar_particles()
            start.organismo.direcao_organimos()
            pygame.display.update()
            CLOCK.tick(15)
            

if __name__ == '__main__':
#    try:
    pygame.init()
    main()
    pygame.quit()
#    except Exception as e:
#        pygame.quit()
#        print(e)
#    finally:
    sys.exit("Saindo..")
