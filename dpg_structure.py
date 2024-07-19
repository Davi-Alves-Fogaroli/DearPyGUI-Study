# The Dgp do 3 things. DPG = Data Processing (?)framework for data harmonisation

# dpg.create_context()
    # Gives to you acesso to any "DPG"" commands
    # If not the first command, "DPG" will not start, and probaly crash 
# dpg.destroy_context()
    # Clear de dpg

# dpg.create_viewport()
    # "ViewPort" is the window created by the operational system
    # Need be create explicit using this comand dpg.create_viewport()
# dpg.show_viewport()
    # Weel this point i asume you now what this comand do kkk
    # But any way i gona register that, because i wanted XP
    # This command show the viewport, whic as customized in line 7: "whih...."

# dpg.setup_dearpygui()
    
# dpg.start_dearpygui()
    # The render loop. Is complestletely handled by the "dpg.start_dearpygui()"
        # This is important, well every comand until this point is impotant, but anyway
        # This is responsible for displaying items (i dont realy undertains waht this mean)
        # Partially maintaining state and callbacks
        # some cases it´s necessaty to explicitly create the render loop
        

import dearpygui.dearpygui as dpg 

dpg.create_context()

dpg.create_viewport(title="?", width=10, height=10)

with dpg.window(label="First Window"):
    dpg.add_text("First gui created wiht success")

dpg.show_viewport()
dpg.setup_dearpygui()
# dpg.start_dearpygui() #if tha comand is up, the while belou dont run (WHY ?)

while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    print("this will run every frame")
    dpg.render_dearpygui_frame()

dpg.destroy_context()

