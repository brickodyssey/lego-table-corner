import math
from solid import *
from solid.utils import *

output_file = 'corner.scad'

# size in mm
corner_height = 30. + 2
corner_size = 43.
wall = 5

table = cube([40,40, 22], center=True)

stud_height = 1.6 + 0.3
stud_diam = 4.8 + 0.3
for i in range(-2,3):
  offset = i*8. + 0.5
  dig = translate([offset, 0, 11 ])(
    cube([stud_diam, 40, stud_height * 2], center=True))
  table += dig

corner = translate([0,0,0.5])(minkowski()(
  cube([corner_size-10, corner_size-10, corner_height/2], center=True),
  cylinder(r=10, h=corner_height/2., center=True)))

size_slant = 100.
offset = size_slant/(2*math.sqrt(2.))
slant = translate([offset,offset,0])(
  rotate(a=45, v=[0,0,1])(
    cube([size_slant, size_slant, 40], center=True)))
side1 = translate([0,30,0])(
  cube([100, 20, 40], center=True))
side2 = translate([30,0,0])(
  cube([20, 100, 40], center=True))

slant += side1 + side2

c = corner - slant - table

# position the final product
final = translate([0,0,27.5])(rotate(a=90, v=[1,0,0])(c))

scad_render_to_file(final, output_file)
