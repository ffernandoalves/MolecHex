import math
from _computer_hexagon import ComputerMatrizShapeHexagon

class PointsPackXY:
    '''
    PointsPackXY
    ============
    Classe para manipulação de listas.\n
    Funções:\n
    + `unpack_xy()` -> return list1, list2\n
    + `pack_xy_once_more(direct=(False, None, None))` -> return list\n
    + `reach_packaging_elements(self, move_axis=[True, 'points_pack', 'position_correction', 'x'])` -> return list1, list2\n
    + `found_points_and_remove()` -> return list, float/int, int\n
    + `found_index_center(points_pack)` -> return int, float/int, int\n
    '''

    def __init__(self, list_pack_xy):
        '''`self.even_moves` e `self.odd_moves` é em relação aos indices das listas dentro do pack'''

        self.list_pack_xy = list_pack_xy
        self.whats_move = ComputerMatrizShapeHexagon()
        
        if self.list_pack_xy:
            self.new_list_pack_xy = self.pack_xy_once_more()
            self.positions_points_removed, self.even_moves, self.odd_moves = self.found_points_and_remove()
            
    def unpack_xy(self, pack=None):
        x_axis = []
        y_axis = []
        
        #talvez essa condição seja desnecessaria 
        if pack:
            pack_ = pack
        else:
            pack_ = self.list_pack_xy

        for i in range(0, len(pack_)):
            lists = pack_[i]

            for j in range(0, len(lists)):
                if j == 0:
                    x_axis.insert(i,lists[j])
                    y_axis.append(lists[j+1])

        return x_axis, y_axis

    def pack_xy_once_more(self, direct=(False, None, None)): #com certeza os None's são as pos_x, pos_y
        '''
        pack_xy_once_more()
        -------------------
        Desempacota uma lista de tuplas, considerando a lista da forma `[(x0, y0),...,(xn, yn)]`.\n
        E, de acordo com o valor da ordenada `y` da tupla, ordena em sub-listas de tuplas, as que\n
        possuírem o mesmo valor em `y`, e transforma em uma nova lista.\n
        Ex:
            ... >>> my_list = [(2, 3), (5, 3), (1, 4), (2, 4), (3, 4)]
            ... >>> my_pack = PointsPackXY(my_list)
            ... >>> my_new_list = my_pack.pack_xy_once_more()
            ... >>> my_new_list
            ... >>> [[(2, 3), (5, 3)], [(1, 4), (2, 4), (3, 4)]]
        '''

        '''
        #TODO
        ------   
        1. Falta verificar para os casos onde todos os valores dentro das tuplas são diferentes.
        \15         - Neste caso, opta-se por deixar da forma: `[[(x0,y0)],[(x1,y1)],...,[(xn,yn)]]`.
            
        \15         - Neste problema somente o último valor da lista fica da forma `[[(x0,y0)]]`.
        \n2. A lista não está sendo ordenada:\n
            Ex:
                ... ... >>> my_list = [(2, 7), (5, 7), (1, 6), (2, 7), (3, 6)]
                ... ... >>> result: [[(2, 7), (5, 7)], [(3, 6)]]
                onde deveria ser:
                ... ... >>> result: [[(2, 7), (2, 7), (5, 7)], [(1, 6), (3, 6)]]
        \ne também da seguinte forma não funciona:
                ... ... >>> my_list = [(2, 7), (5, 7), (1, 6), (2, 4), (3, 6)]
                ... ... >>> result: [[(2, 7), (5, 7)], [(3, 6)]]
                onde deveria ser:
                ... ... >>> result: [[(2, 7), (5, 7)], [(1, 6), (3, 6)], [(2, 4)]]
        \n- Dúvida: Se fazer este passo duas vezes, considerar cada sub-lista como listas e trabalha\n
        somente com as tuplas que encontra nessas sub-listas?\n
        Portanto, somente para valores ordenados e com pelo menos um par (tirando o caso se estiver na última posição da lista) funciona.
        '''

        if direct[0] == False: #para o caso de quiser passar o valores dos pontos x e y diretamente para empacotar
            x, y = self.unpack_xy()
        else:
            x, y = direct[1], direct[2]

        z = 0
        line =[]
        new_list_pack_xy = []
        count_part = 0

        while count_part < len(y):
            
            if z < len(y) - 1:
                if y[z] == y[z+1]:
                    line.append((x[z], y[z]))

                elif y[z] == y[z-1]:
                    line.append((x[z], y[z]))
                    line.append('parte{}'.format(count_part+1))
                    count_part += 1

            else:
                line.append((x[-1], y[-1]))
                line.append('parte{}'.format(count_part +1))
                break

            z += 1

        for i in range(1, count_part + 1):
            m = line[1+line.index('parte{}'.format(i)):line.index('parte{}'.format(i+1))]
            new_list_pack_xy.append(m)

        new_list_pack_xy.insert(0, line[:line.index('parte1')])

        return new_list_pack_xy
    
    def reach_packaging_elements(self, move_axis=[True, 'points_pack', 'position_correction', 'x']):
        '''
        reach_packaging_elements()
        ------------------------
        Está função divide os valores dos elementos do package em duas lista: `pos_x`, `pos_y`. Aplicando
        automaticamente o movimento (soma o a metade da largura da forma geometrica) na lista de pontos do
        eixo x, de acordo com o indices das listas (elemento-lista do package) sejam par ou ímpa.\n
        Se `move_axis[0] == True`, então irá ser usado a lista passada na chamada da classe `PointsPackXY`.\n
        Dessa forma não precisará especificar o resto dos elementos da lista `move_axis`, ou seja, pode ser
        preenchido da seguinte forma: `move_axis=[True, None, None, None]`.'''

        if move_axis[0] == True:
            points_pack = self.positions_points_removed
        else:
            points_pack = move_axis[1]
        
        if (type(move_axis[2]) == int) or (type(move_axis[2]) == float):
            position_correction = move_axis[2]
        else:
            position_correction = 0
            
        if move_axis[3] == 'y':
            #TODO mark - (deffor)
            #A imagem fica deformada. p/ {in_x=False; in_y=True}
            in_x=True
            in_y=False
        else:
            in_x=True
            in_y=False
        
        final_position = []
        pos_x = []
        pos_y = []

        for u in range(0, len(points_pack)):
            list_part = points_pack[u]

            for r in range(0, len(list_part)):
                tupla_posicao = list_part[r]

                for g in range(0, len(tupla_posicao)):

                    if (g == 0) and (move_axis[0] == True):

                        if (in_x == True) and (in_y == False):

                            if u % 2 == 0:
                                pos_x.append(tupla_posicao[g] + self.even_moves)
                                pos_y.append(tupla_posicao[g+1])

                            else:
                                pos_x.append(tupla_posicao[g] + self.odd_moves)
                                pos_y.append(tupla_posicao[g+1])
                        
                        # *(deffor) #
                        elif (in_y == True) and (in_x == False):
                            
                            if u % 2 == 0:
                                pos_x.append(tupla_posicao[g])
                                pos_y.append(tupla_posicao[g+1] + self.even_moves)

                            else:
                                pos_x.append(tupla_posicao[g])
                                pos_y.append(tupla_posicao[g+1] + self.odd_moves)

                    elif g == 0:
                        pos_x.append(tupla_posicao[g] - position_correction)
                        pos_y.append(tupla_posicao[g+1] - position_correction)

        return pos_x, pos_y #posição final das particulas após o movimento da linhas pares em metade do tamanho dos poligonos
    
    def found_points_and_remove(self):
        '''
        found_points_and_remove()
        -------------------------
        Retorna uma matriz com os pontos removidos e a ordem do movimento das linhas na\n
        matriz (listas do package): linhas pares ou impares.\n
        OBS: Foi escolhido o lado direito para serem tirados o maior número de elemendo da matriz.
        '''

        points_pack = self.new_list_pack_xy
        lines_up = []
        line_center = []
        lines_down = []

        index_center, even_moves, odd_moves = self.found_index_center(points_pack)
        count_up = 1
        count_down = 1

        for i in range(0, len(points_pack)):

            #TODO mark - (madness)
            #Dá uma olha nisso tudo..
            if (i < index_center):

                if (count_up-1) % 2 == 0:
                    points_by_bigger_side = math.ceil((count_up-1)/2)
                    points_by_smaller_side = points_by_bigger_side  
                else:
                    points_by_bigger_side = math.ceil((count_up-1)/2)
                    points_by_smaller_side = (count_up-1) - points_by_bigger_side

                line_in_sequen_up = points_pack[index_center - count_up]

                if points_by_smaller_side == 0:
                    lines_up.append(line_in_sequen_up[points_by_bigger_side:-1])

                elif (points_by_smaller_side == 0) and (points_by_bigger_side == 0):
                    lines_up.append(line_in_sequen_up[:-1])

                else:
                    lines_up.append(line_in_sequen_up[points_by_bigger_side:-points_by_smaller_side-1])

                count_up += 1

            elif i == index_center:
                line_center.append(points_pack[index_center])

            elif i > index_center:

                if (count_down-1) % 2 == 0:
                    points_by_bigger_side = math.ceil((count_down-1)/2)
                    points_by_smaller_side = points_by_bigger_side  
                else:
                    points_by_bigger_side = math.ceil((count_down-1)/2)
                    points_by_smaller_side = (count_down-1) - points_by_bigger_side

                line_in_sequen_down = points_pack[index_center + count_down]

                if points_by_smaller_side == 0:
                    lines_down.append(line_in_sequen_down[points_by_bigger_side:-1])

                elif (points_by_smaller_side == 0) and (points_by_bigger_side == 0):
                    lines_down.append(line_in_sequen_down[:-1])

                else:
                    lines_down.append(line_in_sequen_down[points_by_bigger_side:-points_by_smaller_side-1])   

                count_down += 1
                
        new_lines_up = self.sort_(lines_up)
        matriz_esc = new_lines_up + line_center + lines_down

        return matriz_esc, even_moves, odd_moves
    
    def found_index_center(self, points_pack):
        '''
        found_index_center()
        --------------------
        Retorna uma tupla contendo o indice do centro da matriz e a ordem do movimento das linhas na\n
        matriz (listas do package): ordem par ou ímpa'''

        previous_rounding = round((len(points_pack) - 2)/2)
        current_rounding = round(len(points_pack)/2)

        if current_rounding == previous_rounding:
            index_center = math.ceil(len(points_pack)/2) - 1
            odd_moves = self.whats_move.width/2
            even_moves = 0

        else:
            index_center = round(len(points_pack)/2) - 1
            odd_moves = 0
            even_moves = self.whats_move.width/2
        
        return index_center, even_moves, odd_moves
    
    @staticmethod
    def sort_(tuple_in_lists):
        '''Retorna uma nova lista ordenada ao inverso'''

        new_lists = []
        for i in range(1, len(tuple_in_lists)+1):
            new_lists.append(tuple_in_lists[-i])

        return new_lists

if __name__ == '__main__':
    pac = PointsPackXY([(2, 7), (5, 7), (1, 6), (2, 4), (3, 6)])
    print(pac.pack_xy_once_more())
    
#Somente para fins de testes
points_ordem_de_leitura={'''
        [
        [(50, 50), (100, 50), (150, 50), (200, 50), (250, 50),          (300, 50),      (350, 50), (400, 50), (450, 50), (500, 50), (550, 50)],     0
        [(50, 100), (100, 100), (150, 100), (200, 100), (250, 100),     (300, 100),     (350, 100), (400, 100), (450, 100), (500, 100), (550, 100)],1
        [(50, 150), (100, 150), (150, 150), (200, 150), (250, 150),     (300, 150),     (350, 150), (400, 150), (450, 150), (500, 150), (550, 150)],2
        [(50, 200), (100, 200), (150, 200), (200, 200), (250, 200),     (300, 200),     (350, 200), (400, 200), (450, 200), (500, 200), (550, 200)],3
        [(50, 250), (100, 250), (150, 250), (200, 250), (250, 250),     (300, 250),     (350, 250), (400, 250), (450, 250), (500, 250), (550, 250)],4

        [(50, 300), (100, 300), (150, 300), (200, 300), (250, 300),     (300, 300),     (350, 300), (400, 300), (450, 300), (500, 300), (550, 300)],5

        [(50, 350), (100, 350), (150, 350), (200, 350), (250, 350),     (300, 350),     (350, 350), (400, 350), (450, 350), (500, 350), (550, 350)],6
        [(50, 400), (100, 400), (150, 400), (200, 400), (250, 400),     (300, 400),     (350, 400), (400, 400), (450, 400), (500, 400), (550, 400)],7
        [(50, 450), (100, 450), (150, 450), (200, 450), (250, 450),     (300, 450),     (350, 450), (400, 450), (450, 450), (500, 450), (550, 450)],8
        [(50, 500), (100, 500), (150, 500), (200, 500), (250, 500),     (300, 500),     (350, 500), (400, 500), (450, 500), (500, 500), (550, 500)],9
        [(50, 550), (100, 550), (150, 550), (200, 550), (250, 550),     (300, 550),     (350, 550), (400, 550), (450, 550), (500, 550), (550, 550)] 10
        ]
'''}