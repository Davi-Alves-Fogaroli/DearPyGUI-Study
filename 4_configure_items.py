import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Configure items"):

    #configuration is set when button is created
    dpg.add_button(label="Apply", width=300)

    #user data and callback, is created after button was been created
    btn = dpg.add_button(label="Apply 2")
    dpg.set_item_label(btn, "Button 57")
    dpg.set_item_width(btn, 200)

with dpg.window(label="test"):
    dpg.add_button(tag="10", label="t")

dpg.show_item_registry()

dpg.create_viewport(title="Configure items", width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()