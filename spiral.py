#!/usr/bin/env python3
import argparse, math

parser = argparse.ArgumentParser()

parser.add_argument('min_radius', type=float, help='minimum radius (in mm)')
parser.add_argument('max_radius', type=float, help='maximum radius (in mm)')
parser.add_argument('turns', type=int, help='number of turns to perform, between min and max radius')
parser.add_argument('start_angle', type=float, help='angle that the spiral should start at (in radians)')
parser.add_argument('x', type=float, help='displace center of spiral by this x')
parser.add_argument('y', type=float, help='display center of spiral by this y')
parser.add_argument('segments_per_turn', type=int, help='number of segments to render (more is more detailed but takes longer)')

args = parser.parse_args()

min_radius = args.min_radius
max_radius = args.max_radius
turns = args.turns
start_angle = args.start_angle
center_x = args.x
center_y = args.y
segments_per_turn = args.segments_per_turn

tau=(1+5**0.5)/2.0 # golden ratio approx = 1.618033989
#(2-tau)*2*np.pi is golden angle = c. 2.39996323 radians, or c. 137.5 degrees
inc = (2-tau)*2*3.14159 + start_angle
theta=0
k=0.1 # scale factor

# now collect in list 'patches' the locations of all the discs
patches = []
for j in range(turns):
  r = (k*j**0.5) + min_radius
  if r > max_radius:
    break
  theta += inc
  x = center_x + r*math.cos(theta)
  y = center_y + r*math.sin(theta)
  patches.append([x,y])

for idx, patch in enumerate(patches[:-1]):
  currPoint = patch
  nextPoint = patches[idx+1]
  print('({}, {})'.format(patch[0], patch[1]))
