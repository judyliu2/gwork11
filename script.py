import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [0,
              255,
              255]]
    areflect = [0.1,
                0.1,
                0.1]
    dreflect = [0.5,
                0.5,
                0.5]
    sreflect = [0.5,
                0.5,
                0.5]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )
    systems = []
    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 20

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
        print(commands)
        """
        Every opcode is a tuple of the form
        (commandname, parameter, parameter, ...).
        Every symbol is a tuple of the form (type, name).
        """
        #PLUG IN INPUTS FROM COMMAND[1] FOR FUNCTIONS
        for i in range (0, len(p[0])):
                
            if (p[0][i] == "push"):
                systems.append( [x[:] for x in systems[-1]] )
                
            if (p[0][i] == "pop"):
                systems.pop()
                
            if (p[0][i] == "save"):
                save_extension(screen, args[0])

            if (p[0][i] == "display"):
                display(screen)
                
            if (p[0][i] == "sphere"):
                add_sphere(polygons,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step_3d)
                matrix_mult( systems[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []
                
            if (p[0][i] == "torus"):
                add_torus(polygons,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), step_3d)
                matrix_mult( systems[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []

            if (p[0][i] == "box"):
                add_torus(polygons,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), step_3d)
                matrix_mult( systems[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []
                
            if (p[0][i] == "line"):
                add_edge( edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )
                matrix_mult( systems[-1], edges )
                draw_lines(eges, screen, zbuffer, color)
                edges = []

                
            if (p[0][i] == "move"):
                t = make_translate(float(args[0]), float(args[1]), float(args[2]))
                matrix_mult( systems[-1], t )
                systems[-1] = [ x[:] for x in t]

            if (p[0][i] == "scale"):
                t = make_scale(float(args[0]), float(args[1]), float(args[2]))
                matrix_mult( systems[-1], t )
                systems[-1] = [ x[:] for x in t]
                
            if (p[0][i] == "rotate"):
                theta = float(args[1]) * (math.pi / 180)
                if args[0] == 'x':
                    t = make_rotX(theta)
                elif args[0] == 'y':
                    t = make_rotY(theta)
                else:
                    t = make_rotZ(theta)
                matrix_mult( systems[-1], t )
                systems[-1] = [ x[:] for x in t]

            else:
                p_error(p)
                    
    else:
        print "Parsing failed."
        return
