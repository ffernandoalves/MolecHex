from _computer_hexagon import ComputerMatrizShapeHexagon
from _packt_xy import PointsPackXY
from _organismo import Organismo
from _particle import Particle

class Start:
    
    def __init__(self, env_color, dic_color, screen, organism_size=20,
                organism_img=(False, None, None), size_matriz:int = 11,
                hexagonal_shape=True, complete_matrix=False, 
                matrix_shape=['square', 
                (None, #width
                None)]): #height

        self.executando = True
        self.hexagonal_shape = hexagonal_shape
        self.matrix_shape = 'square'
        if matrix_shape[0] == 'rectangular':
            self.matrix_shape = matrix_shape[0]
            self.size_matriz = matrix_shape[1]
        else:
            self.size_matriz = self.checks_matrix_size(size_matriz)
        self.complete_matrix = [complete_matrix, None, None]#pos [0] - True/False; pos [1] - pos_x; pos [2] - pos_y

        self.gera_matriz = ComputerMatrizShapeHexagon(size_matriz = self.size_matriz)
        self.gera_matriz.ordena_particle()
        
        self.pointsXY = PointsPackXY(self.gera_matriz.generated_positions)
        self.complete_matrix[1], self.complete_matrix[2] = self.pointsXY.unpack_xy()
        self.x_new, self.y_new = self.pointsXY.reach_packaging_elements(move_axis=[True, None, None, 'y'])
        
        self.hexInner, self.centerIntHex = self.gera_matriz.computer_vertx_hexagon(self.x_new, self.y_new, whatsHex = 'hexInner')
        self.hexOuter, self.centerExtHex = self.gera_matriz.computer_vertx_hexagon(self.x_new, self.y_new, whatsHex = 'hexOuter')

        self.pos_x = self.x_new[0]
        self.pos_y = self.y_new[0]
        self.organismo = Organismo(self.pos_x, self.pos_y, self.centerIntHex, screen, organism_size, organism_img)

        self.particles = Particle(env_color, dic_color, screen, number_elements=len(self.x_new))
    
    def gerar_particles(self):
        self.particles.creat_particle(
                                    self.hexOuter, self.hexInner, size_matriz = self.size_matriz,
                                    hexagonal_shape = (self.hexagonal_shape, self.x_new, self.y_new),
                                    width = self.gera_matriz.width, height = self.gera_matriz.height,
                                    complete_matrix = self.complete_matrix, matrix_shape=self.matrix_shape)
        return True
    
    def checks_matrix_size(self, size_matriz):
        if type(size_matriz) == int:
            if size_matriz % 2 == 0:
                opc1 = size_matriz + 1
                print('ERRO: Não é aceito números pares. Matriz gerada é de ordem: {0}x{0}'.format(opc1))
            else:
                opc1 = size_matriz
                print('Matriz gerada é de ordem {0}x{0}'.format(opc1))
            return opc1

        elif type(size_matriz) == float:
            opc2 = int(size_matriz)
            print('ERRO: Float atribuido. Matriz gerada pela parte inteira é de ordem: {0}x{0}'.format(opc2))
            if opc2 % 2 == 0:
                opc2 = opc2 + 1
                print('ERRO: Não é aceito números pares. Matriz gerada é de ordem: {0}x{0}'.format(opc2))
            return opc2

        else:
            opc3 = 11
            print('ERRO: Valor não numerico atribuido. Matriz padrão gerada: {0}x{0}'.format(opc3))
            return opc3