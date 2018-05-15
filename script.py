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
        #PLUG IN INPUTS FROM COMMAND[1] FOR FUNCTIONS
        for i in range (0, len(p[0])):
            if (p[0][i] == "COMMENT"):
                p_command_comment(p)
                
            if (p[0][i] == "PUSH" or p[0][i] == "POP"):
                p_command_stack(p)
                
            if (p[0][i] == "SCREEN INT INT" or p[0][i] == "SCREEN"):
                p_command_screen(p)
                
            if (p[0][i] == "SAVE TEXT TEXT"):
                p_command_save(p)

            if (p[0][i] == "DISPLAY"):
                p_command_show(p)
                
            if (p[0][i] == "SPHERE NUMBER NUMBER NUMBER NUMBER" or
                "SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER" or
                "SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL" or
                "SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL"
            ):
                p_command_sphere(p)
                
            if (p[0][i] == "TORUS NUMBER NUMBER NUMBER NUMBER NUMBER" or
                "TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL" or
                "TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER" or
                "TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL"
            ):
                p_command_torus(p)

            if (p[0][i] == "BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER" or
                "BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL" or
                "BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER" or
                "BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL"
            ):
                p_command_box(p)
                
            if (p[0][i] == "LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER" or
                "LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL" or
                "LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER" or
                "LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL" or
                "LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER" or
                "LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL" or
                "LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER" or
                "LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL"
            ):
                p_command_line(p)
                
            if (p[0][i] == "MOVE NUMBERN NUMBER NUMBER SYMBOL" or
                "MOVE NUMBER NUMBER NUMBER"
            ):
                p_command_move(p)

            if (p[0][i] == "SCALE NUMBER NUMBER NUMBER SYMBOL" or
                "SCALE NUMBER NUMBER NUMBER"
            ):
                p_command_scale(p)
                
            if (p[0][i] == "ROTATE XYZ NUMBER SYMBOL" or
                "ROTATE XYZ NUMBER"
            ):
                p_command_rotate(p)
                
            if (p[0][i] == "FRAMES INT"):
                p_command_frames(p)
                
            if (p[0][i] == "BASENAME TEXT"):
                p_command_basement(p)
                
            if (p[0][i] == "VARY SYMBOL INT INT NUMBER"):
                p_command_vary(p)
                
            if (p[0][i] == "SET SYMBOL NUMBER" or
                "SET_KNOBS NUMBER"
            ):
                p_command_knobs(p)
                
            if (p[0][i] == "AMBIENT INT INT INT"):
                p_command_ambient(p)
                
            if (p[0][i] == "CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER" or
                "CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER"
            ):
                p_command_constants(p)
                
            if (p[0][i] == "LIGHT SYMBOL NUMBER NUMBER NUMBER INT INT INT"):
                p_command_light(p)
                
            if (p[0][i] == "SHADING SHADING_TYPE"):
                p_command_shading(p)
                
            if (p[0][i] == "CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER"):
                p_command_camera(p)
                
            if (p[0][i] == "GENERATE_RAYFILES"):
                p_command_generate_rayfiles(p)
                
            if (p[0][i] == "MESH CO TEXT" or
                "MESH SYMBOL CO TEXT"
                "MESH CO TEXT SYMBOL"
                "MESH SYMBOL CO TEXT SYMBOL"):
                p_command_mesh(p)
                
            if (p[0][i] == "SAVE_KNOBS SYMBOL"):
                p_save_knobs(p)
                
            if (p[0][i] == "SAVE_COORDS SYMBOL"):
                p_save_coords(p)
                
            if (p[0][i] == "TWEEN NUMBER NUMBER SYMBOL SYMBOL"):
                p_tween(p)
                
            if (p[0][i] == "FOCAL NUMBER"):
                p_focal(p)
                
            if (p[0][i] == "WEB"):
                p_web(p)
                
            if (p[0][i] == "TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER"):
                p_texture(p)
                
            else:
                p_error(p)
                    
    else:
        print "Parsing failed."
        return
