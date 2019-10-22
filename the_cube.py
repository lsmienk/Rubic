import sys
import mix_cube
l = len(sys.argv)
i = 1
mix = str(sys.argv)

# The Cube starts in its original form. 

y = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
g = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']
b = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
r = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
o = ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
w = ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']

# Go Through the arguments and MIX the cube
while i < l:
    if sys.argv[i] == "F" or sys.argv[i] == "F'" or  sys.argv[i]== "F2":
        mix_cube.f_mix(sys.argv[i], g, b, r, o, w)
    elif sys.argv[i] == "B" or sys.argv[i] == "B'" or  sys.argv[i]== "B2":
        mix_cube.b_mix(sys.argv[i], y, b, r, o, w)
    elif sys.argv[i] == "R" or sys.argv[i] == "R'" or  sys.argv[i]== "R2":
        mix_cube.r_mix(sys.argv[i], y, g, b, r, w)
    elif sys.argv[i] == "L" or sys.argv[i] == "L'" or  sys.argv[i]== "L2":
        mix_cube.l_mix(sys.argv[i], y, g, b, o, w)
    elif sys.argv[i] == "U" or sys.argv[i] == "U'" or  sys.argv[i]== "U2":
        mix_cube.u_mix(sys.argv[i], y, g, r, o, w)
    elif sys.argv[i] == "D" or sys.argv[i] == "D'" or  sys.argv[i]== "D2":
        mix_cube.d_mix(sys.argv[i], y, g, b, r, o)
    else:
        print("invalid input")
    i += 1
    
#print(y, g, b, r, o, w)

# Algorithm to solve the cube. 
