try:
	import Image
except ImportError:
	from PIL import Image
import random
import argparse

p = argparse.ArgumentParser(description="Generate an elementary cellular automaton")
p.add_argument("-x", "--width", help="Width", default=322)
p.add_argument("-y", "--height", help="Height", default=322)
p.add_argument("-r", "--rulenumber", help="Rule number", default=18)
p.add_argument("-o", "--outputfile", help="Output file", default="out.png")
p.add_argument("-s", "--scalefactor", help="Scale the output image by an interger amount", default=1)
args = p.parse_args()

width = int(args.width)
height = int(args.height)
rulenumber = int(args.rulenumber)
scalefactor = int(args.scalefactor)

# Define colors of the output image
true_pixel = (255, 255, 255)
false_pixel = (0, 0, 0)

# Generates a dictionary that tells you what your state should be based on the rule number and the states of the adjacent cells in the previous generation
def generate_rule(rulenumber):
	rule = {}
	for left in [False, True]:
		for middle in [False, True]:
			for right in [False, True]:
				rule[(left, middle, right)] = rulenumber%2 == 1
				rulenumber //= 2
	return rule

# Generates a 2d representation of the state of the automaton at each generation
def generate_ca(rule):
	ca = []
	# Initialize the first row of ca randomly
	ca.append([])
	for x in range(width):
		ca[0].append(bool(random.getrandbits(1)))

	# Generate the succeeding generation
	# Cells at the edges are initialized randomly
	for y in range(1,height):
		ca.append([])
		ca[y].append(bool(random.getrandbits(1)))
		for x in range(1, width-1):
			ca[y].append(rule[(ca[y-1][x-1], ca[y-1][x], ca[y-1][x+1])])
		ca[y].append(bool(random.getrandbits(1)))
	return ca

rule = generate_rule(rulenumber)
ca = generate_ca(rule)

new = Image.new('RGB', [width, height])

print("Placing pixels...")
for y in range(height):
	for x in range(width):
		new.putpixel((x, y), true_pixel if ca[int(y/scalefactor)][int(x/scalefactor)] else false_pixel)

print("Saving image...")
new.save(args.outputfile)
print("Done!")




    # converts integer rulenumber to binary list of rules
    def generate_rules(ruleNumber):
        if rulenumber >= 0 and ruleNumber < 256
            rule = [int(i) for (i) in list('{0:0b}'.format(ruleNumber))]
        else
            rule = [0,0,0,0,0,0,0,0]

    # neighbors: binary array [left, center, right]
    # integer produced by binary representation of neighbors is index in rules array
    def apply_rule(rule, neighbors):
        index = int("".join(str(x) for x in neighbors), 2)
        return rule[index]


    def run_rules(rule):
        # initialize the first row of ca randomly
        self.cells.append([])
        for x in range(self.grid_width):
            self.cells[0].append(bool(random.getrandbits(1)))

        # generate succeeding generation
        for y in range(1, self.grid_height):
            self.cells.append([])
            self.cells.append(bool(random.getrandbits(1)))
            for x in range(1, self.grid_width - 1):
                self.cells[y].append(rule[])

    def get_cell_value(self, row, col): #used to take sum of all cells around
        #if on the screen
        if row >= 0 and row < self.grid_height and col >= 0 and col < self.grid_width:
           return self.cells[row][col]
        return 0

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
for y in range(1, self.grid_height):
    self.cells.append([])
    self.cells[y].append(random.getrandbits(1))
    for x in range(0, self.grid_width - 1):
        neighbors = self.get_neighbors(x,y)
        #self.cells[y].append(self.apply_rule(neighbors))
        self.cells[y].append(random.getrandbits(1))
    #self.cells[y].append(bool(random.getrandbits(1)))        
