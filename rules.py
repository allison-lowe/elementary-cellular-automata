import random
import pyglet

class Rules:

    def __init__(self, window_width, window_height, cell_size, number):
        self.grid_width = int(window_width / cell_size)
        self.grid_height = int(window_height / cell_size)
        self.cell_size = cell_size
        self.rule = [0,0,0,0,0,0,0,0]
        self.rulenumber = number
        self.cells = []
        self.generate_ca()

    def generate_rules(self):
        if self.rulenumber >= 0 and self.rulenumber < 256:
            self.rule = [int(i) for (i) in list('{0:0=8b}'.format(self.rulenumber))]

    def apply_rule(self, neighbors):
        neighbors = neighbors * 1
        index = int("".join(str(x) for x in neighbors), 2)
        return self.rule[index]

    def get_neighbors(self, x, y):
        #if x > 0 and x < self.grid_width - 1 and y > 0 and y < self.grid_height - 1:
        return ([self.cells[y][x-1],
                self.cells[y][x],
                self.cells[y][x+1]])

    def generate_ca(self):
        self.generate_rules()

        # initialize first row of CA randomly
        for x in range(0, self.grid_width):
            self.cells.append([])
            # self.cells[0].append(random.getrandbits(1))
            self.cells[0].append(0) # set first index all to 0

        #set middle index = 1
        self.cells[0][int(self.grid_width/2)] = 1

        # generate succeeding generation
        for y in range(0, self.grid_height - 1):
            #self.cells[y+1].append(random.getrandbits(1))
            self.cells[y+1].append(0)
            for x in range(1, self.grid_width - 1):
                neighbors = self.get_neighbors(x,y)
                self.cells[y+1].append(self.apply_rule(neighbors))
                # self.cells[y].append(random.getrandbits(1))
            #self.cells[y+1].append(random.getrandbits(1))
            self.cells[y+1].append(0)

    def draw(self):
        for row in range(0,self.grid_height):
            for col in range(0,self.grid_width):
                if self.cells[row][col] == 1:
                    #(0,0) (0, 20) (20,0) (20,20)
                    square_coords = (row * self.cell_size,                  col * self.cell_size,
                                     row * self.cell_size,                  col * self.cell_size + self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size + self.cell_size)
                    pyglet.graphics.draw_indexed(4,pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 1, 2, 3],
                                     ('v2i', square_coords))
