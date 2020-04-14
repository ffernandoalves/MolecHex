import math

class ComputerMatrizShapeHexagon:
    def __init__(self, size_matriz = 11):
        #Initial particle position, particle size, particle matrix size
        self.Px_0 = 50
        self.Py_0 = 50
        #self.width = math.sqrt(3/2)*self.height/2
        self.width = 50 #particle
        self.height = 50 #
        self.size = (self.width, self.height)
        
        #Functional for rectangular matrices, but generates only matrices of square particles.
        #Tipo quadrada -- 
        if type(size_matriz) == int:
            self.size_matriz = size_matriz
            self.width_matriz = self.size_matriz
            self.height_matriz = self.size_matriz
        #Tipo retangular -- 
        if (type(size_matriz) == list) or (type(size_matriz) == tuple):
            self.size_matriz = size_matriz
            self.width_matriz = self.size_matriz[0]
            self.height_matriz = self.size_matriz[1]

        #list of all points in the matrix
        self.generated_positions = []
    
    def ordena_particle(self):
        x_new = self.Px_0
        y_new = self.Py_0

        for i in range(0, self.width_matriz):
            for j in range(0, self.height_matriz):
                if j > i:
                    x_new += self.width
                elif i == j:
                    x_new = y_new
                else: # i > j
                    x_new += self.width
                    if j == 0:
                        x_new = self.Px_0
                        y_new += self.height

                self.generated_positions.append((x_new, y_new))

        return True

    def computer_vertx_hexagon(self, X0, Y0, **kwargs):
        whatsHex = None
        l = self.height/2
        a = self.width/2
        hex_points = []
        center_xy_hex = []
        
        #hex_points = [(x0, y0), (x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]
        for key, value in kwargs.items():
            if key == 'whatsHex':
                whatsHex = value
        
        if whatsHex == 'hexOuter':

            for i in range(0, len(X0)):
                for j in range(0, len(Y0)):
                    if j == i:

                        x = X0[i]
                        y = Y0[j]
                        hex_points.append([(x + 2 * a -1, y + l +5.5), 
                                            (x + a, y + 3*l/2 +5), (x +1, y + l +5.5), 
                                            (x +1, y -5.5), (x + a, y - l/2 -5), 
                                            (x + 2 * a -1, y -5.5)])
                        center_xy_hex.append([(x + a, y + l/2)])    

            return hex_points, center_xy_hex

        elif whatsHex == 'hexInner':
        
            for i in range(0, len(X0)):
                for j in range(0, len(Y0)):
                    if j == i:

                        x = X0[i]
                        y = Y0[j]
                        hex_points.append([(x + 2 * a -6, y + l +1), 
                                            (x + a, y + 3*l/2 -2), (x +6, y + l +1), 
                                            (x +6, y -1), (x + a, y - l/2 +2), 
                                            (x + 2 * a -6, y -1)])
                        center_xy_hex.append([(x + a, y + l/2)])    

            return hex_points, center_xy_hex
