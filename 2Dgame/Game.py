import os
import platform


if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"


import framework
import first_state
from pico2d import*

open_canvas()

framework.run(first_state)

close_canvas()