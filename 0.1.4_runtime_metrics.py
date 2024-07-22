# Runtime metrics show the performance of your app in real-time. Here is it shown in conjunction with the built-in 
# style editor.set
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

dpg.show_metrics()
dpg.show_style_editor()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()