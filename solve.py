import mix_cube

def solve(y, g, b, r, o, w):
    mix_cube.u_mix("U", y, g, r, o, w)
    mix_cube.r_mix("R2", y, g, b, r, w)
    mix_cube.f_mix("F", g, b, r, o, w)
    mix_cube.b_mix("B", y, b, r, o, w)
    mix_cube.r_mix("R", y, g, b, r, w)
    mix_cube.b_mix("B2", y, b, r, o, w)
    mix_cube.r_mix("R", y, g, b, r, w)
    mix_cube.u_mix("U2", y, g, r, o, w)
    mix_cube.l_mix("L", y, g, b, o, w)
    mix_cube.b_mix("B2", y, b, r, o, w)
    mix_cube.r_mix("R", y, g, b, r, w)
    mix_cube.u_mix("U'", y, g, r, o, w)
    mix_cube.d_mix("D'", y, g, b, r, o)
    mix_cube.r_mix("R2", y, g, b, r, w)
    mix_cube.f_mix("F", g, b, r, o, w) 
    mix_cube.r_mix("R'", y, g, b, r, w)
    mix_cube.l_mix("L", y, g, b, o, w)
    mix_cube.b_mix("B2", y, b, r, o, w)
    mix_cube.u_mix("U2", y, g, r, o, w)
    mix_cube.f_mix("F2", g, b, r, o, w)
