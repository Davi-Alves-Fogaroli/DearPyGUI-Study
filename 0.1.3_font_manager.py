# The font manager shows all loaded fonts and their appropriate sizes. It allows you to inspect all characters, 
# or glyphs, that are loaded with each font file.
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

dpg.show_font_manager()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()