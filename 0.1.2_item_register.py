# The item registry shows all items of a running application in a hierarchical structure. For each item, 
# a number of details, such as its tag ID, are shown.
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

dpg.show_item_registry()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()