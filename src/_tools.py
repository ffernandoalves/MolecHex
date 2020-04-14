import pygame
from _textos import Texto


BOTTON_BAR = 40

class Tools:
    def __init__(self, env_color, dic_color, width, height, screen):
        self.screen = screen
        self.width, self.height = width, height
        self.env_color = env_color
        self.dic_color = dic_color
        #self.bottom_bar()

        self.pos_x = None
        self.pos_y = None
        self.size_bar = 50
        self.mouse_x = None
        self.mouse_y = None #pygame.mouse.get_pos()
        #self.reac = Reacao()
        #self.matrix = Start()
        self.count = [0]
        self.doble = False
        #-
        #self.distance_x_r = lambda per: (self.width * per)/ 100 #fixed on the right
        #self.distance_x_l = lambda per: (self.width * per)/ 100 #fixed on the left

        #self.text_position_x_axis = self.width
        #self.shade_position_x_axis = self.text_position_x_axis - 1

        self.text_position_y_axis = self.height - 37
        self.shade_position_y_axis =  self.text_position_y_axis + 1
    
    def distance_per(self, per, dis='w'):
        '''
        + `dis = 'w'` para calcular a posição da largura
        + `dis = 'h'` para calcular a posição da altura
        '''
        if dis == 'w':
            dis = (self.width * per) / 100
        elif dis == 'h':
            dis = (self.height * per) / 100
        
        return dis
    
    def bottom_bar(self):
        #try:
        pygame.draw.rect(self.screen, self.env_color[2][1], [0, self.height - BOTTON_BAR, self.width, BOTTON_BAR])
        #return True
        '''except:
            pass'''

    def direcao(self):
        text_position_x_axis = self.distance_per(1.12, dis='w')
        shade_position_x_axis = text_position_x_axis - 1
        text_position_y_axis = self.distance_per(95.38, dis='h')#self.height - 37
        shade_position_y_axis =  text_position_y_axis + 1

        pygame.draw.rect(self.screen, self.env_color[2][1], [0, self.height - BOTTON_BAR, self.width, BOTTON_BAR])
        textoPlacarSombra = Texto("Posição: ({0}, {1})".format(self.pos_x, self.pos_y), self.env_color[0][1], 25, self.screen)
        textoPlacarSombra.show(shade_position_x_axis, text_position_y_axis)
        textoPlacar = Texto("Posição: ({0}, {1})".format(self.pos_x, self.pos_y), self.env_color[1][1], 25, self.screen)
        textoPlacar.show(text_position_x_axis, shade_position_y_axis)
    
    def menu_moleculas(self):
        x = 800
        y = [150]
        id_pos_cor = []

        for i in range(0, len(self.dic_color)):
            id_color = self.dic_color[i]
            for j in range(0, len(id_color)):
                y.append(y[-1] + self.size_bar + 5)
                pygame.draw.rect(self.screen, id_color[1], [x, y[i], self.size_bar, self.size_bar])
            id_pos_cor.append([(x, y[i]), id_color[1], id_color[0]])
        
        #return id_pos_cor
        '''self.count = self.change_color_by_molecula(id_pos_cor)
        #if self.doble == True:
        #    self.count.append(self.count[-1]+ 1)
        pygame.draw.rect(self.screen, self.dic_color[0][1], [x - 175, y[0], 3*self.size_bar, self.size_bar])
        textoCliquesSombra = Texto("Cliques: {}".format(self.count[-1]), self.env_color[0][1], 25, self.screen)
        textoCliquesSombra.show(x -175, y[0])
        textoCliques = Texto("Cliques: {}".format(self.count[-1]), self.env_color[2][1], 25, self.screen)
        textoCliques.show(x - 175, y[0])'''
    
    def matrix_original(self):
        posX = 620
        posY = 695
        pygame.draw.rect(self.screen, self.env_color[6][1], [posX, posY, 5*self.size_bar, self.size_bar])
        textoPlacarSombra = Texto("Matriz Quadrada", self.env_color[0][1], 25, self.screen)
        textoPlacarSombra.show(644, self.height - 100)
        textoPlacar = Texto("Matriz Quadrada", self.env_color[2][1], 25, self.screen)
        textoPlacar.show(645, self.height - 99)
        matriz_hexa = False
        if posX < self.mouse_x < posX + 5*self.size_bar and posY < self.mouse_y < posY + self.size_bar:
            '''if pygame.mouse.get_pressed()[0]:
                self.matrix.main(matriz_hexa = False)
            elif pygame.mouse.get_pressed()[1]:
                self.matrix.main(matriz_hexa = True)'''
            pass

    def change_color_by_molecula(self, id_pos_cor):
        #id_pos_cor = self.menu_moleculas()
        posXY = []
        posX = []
        posY = []
        cor_in = []

        for i in range(0, len(id_pos_cor)):
            id_color = id_pos_cor[i]
            posXY.append(id_color[0])
            cor_in.append(id_color[2])

        for l in range(0, len(posXY)):
            intuple_ = posXY[l]
            posX.append(intuple_[0])
            posY.append(intuple_[1])
        
        if posX[0] < self.mouse_x < posX[0] + self.size_bar and posY[0] < self.mouse_y < posY[0] + self.size_bar:
            if pygame.mouse.get_pressed()[0]:
                print('cor ativada: {}'.format(cor_in[0]))
                self.count.append(self.count[-1]+ 1)
                return self.count
                '''if self.doble == True and pygame.mouse.get_pressed()[0]:
                print('cor desativada: {}'.format(cor_in[0]))
                self.doble = False
                return self.count.append(self.count[-1]+ 1)'''
            else:
                return self.count
        else:
            return self.count
    
    def Cursor(self):  
        #pygame.draw.rect(self.screen, self.env_color[6][1], [posX, posY, 5*self.size_bar, self.size_bar])
        text_position_x_axis = self.distance_per(1.12, dis='w')
        shade_position_x_axis = text_position_x_axis - 1
        text_position_y_axis = self.distance_per(95.38, dis='h')#self.height - 37
        shade_position_y_axis =  text_position_y_axis + 1

        textoPlacarSombra = Texto("Cursor: ({0}, {1})".format(self.mouse_x, self.mouse_y), self.env_color[0][1], 25, self.screen)
        textoPlacarSombra.show(644, text_position_y_axis)
        textoPlacar = Texto("Cursor: ({0}, {1})".format(self.mouse_x, self.mouse_y), self.env_color[1][1], 25, self.screen)
        textoPlacar.show(645, shade_position_y_axis)