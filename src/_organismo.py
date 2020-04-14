import pygame

from _packt_xy import PointsPackXY


BLACK=(0,0,0)

#Tamanho do organismo
TAMANHO = 20

class Organismo:
    def __init__(self, x, y, posCenter, screen, organism_size = TAMANHO, organism_img = (False, None, None)):
        self.screen = screen
        self.organism_img = organism_img
        self.organism_size = organism_size
        self.position_correction = self.organism_size/2
        
        self.pointsXY = PointsPackXY(None)
        self.center_x, self.center_y = self.pointsXY.reach_packaging_elements(move_axis=[False, posCenter, self.position_correction, None])
        self.packed_centers = self.pointsXY.pack_xy_once_more(direct=(True, self.center_x, self.center_y))

        self.x = self.center_x[0] #index center 45 11x11
        self.y = self.center_y[0] #index center 45 11x11

        self.centerHexagono = [self.x, self.y]
        self.organismo = [self.centerHexagono]
        self.comp = 1
        self.direcao = ""
        self.posicaoatual=[]

    def tail_off(self, tail='off'):
        self.add_point_in_organism()
        if tail == 'off':
            while len(self.organismo) > self.comp:
                del self.organismo[0]
        elif tail == 'on':
            pass
        return 0
    
    def add_point_in_organism(self, direction=''):
        #self.tail_off(tail='off')
        #self.direcao
        my_step = 0
        local_index = 0
        permitted_positions = []
        for i in range(len(self.packed_centers)):
            line = self.packed_centers[i]
            for j in range(len(line)):
                count_steps = j
                points = line[j]
                permitted_positions.append([list(points), i, count_steps])

                #print(list(points))
                #if self.direcao == 'direita':
                    #if 
                    #self.x = permitted_positions[j][0][0]
                    #self.organismo.append([self.x, self.y])

        index='None'
        for k in range(len(permitted_positions)):
            posistion_addr = permitted_positions[k]
            for r in range(len(self.organismo)):
                if self.organismo[r] in posistion_addr:
                    #index = permitted_positions[0].index(self.organismo[0])
                    index = posistion_addr[1]
                    #print(index)
                    #print(posistion_addr)
        
        #print(permitted_positions)

        self.organismo.append([self.x, self.y])
        return {'ADDED'}

    def show(self):
        for XY in self.organismo:
            if self.organism_img[0] == True:
                org_pic = pygame.transform.scale(self.organism_img[1], self.organism_img[2])
                self.screen.blit(org_pic, (XY[0], XY[1]))
            else:
                pygame.draw.rect(self.screen, BLACK, (XY[0], XY[1], self.organism_size, self.organism_size))
        #print(self.organismo)

    def direcao_organimos(self):
        
        if self.direcao == "cima":
            self.y -= self.organism_size
            #self.y = self.center_y[self.center_y.index(self.y) - 1]
            self.tail_off(tail='off')
            #print(f'Posição y: {self.y}; Indice: {self.center_y.index(self.y)}')

            #self.add_point_in_organism(tail='off')

        elif self.direcao == "baixo":
            self.y += self.organism_size
            #self.y = self.center_y[self.center_y.index(self.y) + 1]
            self.tail_off(tail='off')
            #print(f'Posição y: {self.y}; Indice: {self.center_y.index(self.y)}')

            #self.add_point_in_organism(tail='off')

        elif self.direcao == "esquerda":
            self.x -= self.organism_size
            #self.x = self.center_x[self.center_x.index(self.x) - 1]
            self.tail_off(tail='off')
            #print(f'Posição x: {self.x}; Indice: {self.center_x.index(self.x)}')

            #self.add_point_in_organism(tail='off')

        elif self.direcao == "direita":
            self.x += self.organism_size
            #self.x = self.center_x[self.center_x.index(self.x) + 1]
            self.tail_off(tail='off')
            #print(f'Posição x: {self.x}; Indice: {self.center_x.index(self.x)}')

            #self.add_point_in_organism(tail='off')

        elif self.direcao == "parado":
            self.x = self.x
            self.y = self.y
            self.tail_off()
            #self.add_point_in_organism()
        else:
            pass
        #self.tail_off()
        self.show()