import ctypes
from ctypes import c_int
import win32gui, win32con
from win32api import GetSystemMetrics
import dearpygui.dearpygui as dpg

#Set up DWM API
dwm = ctypes.windll.dwmapi
width, height = GetSystemMetrics(0),GetSystemMetrics(1)

class Margins(ctypes.Structure):
    _fields_ = [
        ("cxLeftWidth",c_int),
        ("cxRightWidth",c_int),
        ("cyTopHeight",c_int),
        ("cyBottomHeight",c_int),
    ]

dpg.create_context()

with dpg.window(label="Transcription:", pos= [width*0.85,height*0.05]):
    dpg.add_text("Does this still work?")

#create a borderless transparent viewport
dpg.create_viewport(
    title="TransparentOverlay",
    x_pos=0,
    y_pos=0,
    width=width,
    height=height,
    decorated=False,
    always_on_top=True,
    clear_color=[0,0,0,0],

)

dpg.setup_dearpygui()
dpg.show_viewport()

#Grab the OS-level window handle
hwnd = win32gui.FindWindow(None, "TransparentOverlay")
#Extend the frame to fill the entire client area
m = Margins(-1,-1,-1,-1)
dwm.DwmExtendFrameIntoClientArea(hwnd, ctypes.byref(m))

#Making it click through
styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(hwnd,win32con.GWL_EXSTYLE, styles | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)

while dpg.is_dearpygui_running():
    width= GetSystemMetrics(0),
    height= GetSystemMetrics(1),
    dpg.render_dearpygui_frame()

dpg.destroy_context()
