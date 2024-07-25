import dearpygui.dearpygui as dpg

dpg.create_context()


dpg.show_documentation()

dpg.show_style_editor()

# The built-in style editor allows you to experiment with all style options at runtime to find the exact colors, 
# padding, rounding and other style settings for your application. You can use the sliders to change the settings, 
# which are applied to all items in your app, so you can immediately see what effect the changes have on your GUI.

dpg.show_debug()

dpg.show_about()

dpg.show_metrics()

dpg.show_font_manager()
# The font manager shows all loaded fonts and their appropriate sizes. It allows you to inspect all characters, 
# or glyphs, that are loaded with each font file.

dpg.show_item_registry()
# The item registry shows all items of a running application in a hierarchical structure. For each item, 
# a number of details, such as its tag ID, are shown.


# dpg.show_item_registry()
# dpg.show_debug()
# dpg.show_documentation()
# dpg.show_style_editor()
# dpg.show_about()
# dpg.show_metrics()
# dpg.show_font_manager()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()