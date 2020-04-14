import sys
import pygame
import random

class Particle:
    def __init__(self, env_color, dic_color, screen, number_elements=1):
        self.screen = screen
        self.env_color = env_color
        self.dic_color = dic_color
        self.thickness = 1
        self.radius = 28
        
        cor =[color[1] for color in self.dic_color]
        self.random_color = random.choices(cor, k=number_elements)
        self.random_ = [(155, 209, 205), (0,0,0)]

    def square(self, color, position):
        #pygame.draw.rect(screen, color, (x,y,width,height), thickness)
        pygame.draw.rect(self.screen, color, position, self.thickness)
    
    def circle(self, color, position):
        #pygame.draw.circle(screen, color, (x,y), radius, thickness)
        pygame.draw.circle(self.screen, color, position, self.radius, self.thickness)
    
    def polyg(self, color, position):
        pygame.draw.polygon(self.screen, color, position)

    def creat_particle(self, posExterior, posInterior, size_matriz = 11, **kwargs):
        lol = False
        try:
            matrix_shape = 'square'
            hexagonal_shape = [True, None, None]
            complete_matrix = [False, None, None]

            for key, value in kwargs.items():
                if key == 'hexagonal_shape':
                    hexagonal_shape = value
                    pos_x = hexagonal_shape[1]
                    pos_y = hexagonal_shape[2]
                if key == 'width':
                    width = value
                if key == 'height':
                    height = value
                if key == 'size_matriz':
                    size_matri = value
                if key == 'matrix_shape':
                    matrix_shape = value
                if key == 'complete_matrix':
                    complete_matrix = value
                    all_pos_x = complete_matrix[1]
                    all_pos_y = complete_matrix[2]
                    
            if matrix_shape == 'square':
                if (hexagonal_shape[0] == True) and (complete_matrix[0] == False) :
                    #Mostra a matriz de particulas hexagonal, com elementos retirados
                    for i in range(len(posInterior)):
                        #self.polyg(self.env_color[0][1], posExterior[i])
                        #self.polyg(self.env_color[6][1], posInterior[i])
                        #for j in range(len(self.random_color)):
                            #self.polyg(self.random_color[j], posExterior[i])
                            #self.polyg(self.random_color[j], posInterior[i])
                        self.polyg(self.dic_color[5][1], posExterior[i])
                        self.polyg(self.dic_color[1][1], posInterior[i])
                        
                elif (hexagonal_shape[0] == False) and (complete_matrix[0] == False):
                    #Mostra a matriz de particulas quadrada, com elementos retirados
                    for i in range(0, len(pos_x)):
                        self.square(self.env_color[0][1], (pos_x[i], pos_y[i], width, height))

                elif (complete_matrix[0] == True) and (hexagonal_shape[0] == False):
                    #Mostra a matriz de particulas quadrada, sem elementos retirados
                    for i in range(0, len(all_pos_x)):
                        self.square(self.env_color[0][1], (all_pos_x[i], all_pos_y[i], width, height))
            
            elif matrix_shape == 'rectangular':
                for i in range(0, len(all_pos_x)):
                    self.square(self.env_color[0][1], (all_pos_x[i], all_pos_y[i], width, height))

        except Exception as e:
            lol = e
            print(e)
        finally:
            if lol:
                sys.exit()