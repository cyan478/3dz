from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()

for i in range(500):
		for j in range(500):
				R = (i+j) % 256
				G = (i*j) % 256
				B = (i-j) % 256
				color = [ R, G, B ]
				
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', edges, transform, screen, color )