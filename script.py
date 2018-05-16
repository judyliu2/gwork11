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
    systems = [tmp]
    edges =[]
    polygons = []
    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 20

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    
        """
        Every opcode is a tuple of the form
        (commandname, parameter, parameter, ...).
        Every symbol is a tuple of the form (type, name).
        """
        for args in commands:
            if (args[0] != 'rotate' and args[0] != 'save' and args[0] !='display'):
                temp = [args[0]]
                for a in args[1:]:
                    if isinstance(a, float):
                        temp.append(a)
                args = tuple(temp)
                
            operation = args[0]
            
            if (operation == 'push'):
                systems.append( [x[:] for x in systems[-1]] )
                
            elif (operation == 'pop'):
                systems.pop()
                
            elif (operation == 'display' or operation == 'save'):
                if (operation == 'display'):
                    display(screen)
                else:
                    save_extension(screen, args[1]+args[2])
                    
                
            elif (operation == 'sphere'):
                add_sphere(polygons,
                       float(args[1]), float(args[2]), float(args[3]),
                       float(args[4]), step_3d)
                matrix_mult( systems[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []
                
            elif (operation == 'torus'):
                add_torus(polygons,
                      float(args[1]), float(args[2]), float(args[3]),
                      float(args[4]), float(args[5]), step_3d)
                matrix_mult( systems[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []

            elif (operation == 'box'):
                add_box(polygons,
                    float(args[1]), float(args[2]), float(args[3]),
                    float(args[4]), float(args[5]), float(args[6]))
                matrix_mult( systems[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []
                
            elif (operation == 'line'):
                add_edge( edges,
                      float(args[1]), float(args[2]), float(args[3]),
                      float(args[4]), float(args[5]), float(args[6]) )
                matrix_mult( systems[-1], edges )
                draw_lines(edges, screen, zbuffer, color)
                edges = []

                
            elif (operation == 'move'):
    
                t = make_translate(float(args[1]), float(args[2]), float(args[3]))
                matrix_mult( systems[-1], t )
                systems[-1] = [ x[:] for x in t]

            elif (operation == 'scale'):
                t = make_scale(float(args[1]), float(args[2]), float(args[3]))
                matrix_mult( systems[-1], t )
                systems[-1] = [ x[:] for x in t]
                
            elif (operation == 'rotate'):
                theta = float(args[2]) * (math.pi / 180)
                if args[1] == 'x':
                    t = make_rotX(theta)
                elif args[1] == 'y':
                    t = make_rotY(theta)
                else:
                    t = make_rotZ(theta)
                matrix_mult( systems[-1], t )
                systems[-1] = [ x[:] for x in t]

                    
    else:
        print "Parsing failed."
        return
