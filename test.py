import random


    def generate_rules(self):
        if rulenumber >= 0 and rulenumber < 256:
            rule = [int(i) for (i) in list('{0:0=8b}'.format(rulenumber))]

    def apply_rule(self, neighbors):
        index = int("".join(str(x) for x in neighbors), 2)
        return self.rule[index]

    def get_neighbors(self, x, y):
        if x > 0 and x < self.grid_width and y > 0 and y < self.grid_height:
        return ([self.cells[x-1][y-1],
                 self.cells[x][y-1],
                 self.cells[x+1][y-1]])

    def generate_ca(self):
        self.generate_rules()

        # initialize first row of CA randomly
        self.cells.append([])
        for x in range(0, self.grid_width):
            self.cells[0].append(bool(random.getrandbits(1)))

        # generate succeeding generation
        for y in range(1, self.grid_height):
            self.cells.append([])
            self.cells[y].append(bool(random.getrandbits(1)))
            for x in range(1, self.grid_width - 1):
                neighbors = self.get_neighbors(x,y)
                self.cells[y].append(applyRule(self,neighbors))
            self.cells[y].append(bool(random.getrandbits(1)))

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
