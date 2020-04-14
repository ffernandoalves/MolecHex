import pygame

class Texto:
    '''Possível formato de chamada da classe:\n
    `textoParticle = Texto("(" + str(pos_y[i]) + ", " + str(pos_x[i]) + ")", color, size_font)`'''
    def __init__(self, msg:str, cor, tam:int, screen):
        self.font = pygame.font.SysFont('comicsansms', tam)
        self.texto = self.font.render(msg, True, cor)
        self.screen = screen
        
    def show(self, x, y):
        self.screen.blit(self.texto, [x, y])
        return True