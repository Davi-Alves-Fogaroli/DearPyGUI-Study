# The built-in style editor allows you to experiment with all style options at runtime to find the exact colors, 
# padding, rounding and other style settings for your application. You can use the sliders to change the settings, 
# which are applied to all items in your app, so you can immediately see what effect the changes have on your GUI.
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

dpg.show_style_editor()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()