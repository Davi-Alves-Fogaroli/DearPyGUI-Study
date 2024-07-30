import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

dpg.create_context()

with dpg.window(label='window 2', width=300, pos=(320,10)):
    title_color = (0,255,0,255)
# with dpge.movable_group('I can\'t be moved to the left', same_window_only=True, title_color=title_color):
    with dpg.tab_bar(label="tab_bar"):
        with dpg.tab(label="tab1"):
            dpg.add_button(label='A button') 
        with dpg.tab(label="tab2"):
            dpg.add_text('... and some text')

# with dpge.movable_group('Don\'t even try window 1', same_window_only=True, title_color=title_color):
#     dpg.add_slider_floatx(label='vector1', size=3)
#     dpg.add_slider_floatx(label='vector2', size=3)
#     dpg.add_slider_floatx(label='vector3', size=3)

# with dpge.movable_group('But I can be moved within this window!', same_window_only=True, title_color=title_color):
#     dpg.add_input_text(label='Email', default_value='user@email.com')
#     dpg.add_input_text(label='Password', default_value='123456789', password=True)


dpg.create_viewport()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()