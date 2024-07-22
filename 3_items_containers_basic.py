#  RUN ORTOGRAPCH CORRECTOR
# Creating items, with many ways, creatin containers and parent 
# Itens have ottwer cofigurations
    # get_item_configuration
    # get_item_state
    # get_item_info

import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Items and Containers"):
    b0 = dpg.add_button(label="Button 0")
    b1 = dpg.add_button(tag=100, label="Button 1")
    dpg.add_button(tag="Btg2", label="Button 2")
    with dpg.group():
        dpg.add_button(label="Button 3")
        dpg.add_button(label="Button 4")
        with dpg.group() as group1:
            pass


dpg.add_button(label="Button 6", parent=group1)
dpg.add_button(label="Button 7", parent=group1)


print("Botão 'b0': ", b0)
print("Botão 'b1': ", b1)
print("Botão definido por tag: ", dpg.get_item_label("Btg2"))


dpg.create_viewport(title='Itenms and Containers', width=600, height=600)
dpg.show_viewport()
dpg.setup_dearpygui()
dpg.start_dearpygui()
dpg.destroy_context()