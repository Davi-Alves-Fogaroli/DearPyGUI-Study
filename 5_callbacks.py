# we can add functions and methods to itens whem there are createds ou lated, using command -> set_item_callback

# Callbacks may have up to 3 args, in order:
    # Sender
        # id of the UI item that submitted the callback
    # app_data:
        # occasionally UI items will send their won data (ex. file dialog)
    # user_data:
        #any python object you want to send to the function

# More information of itens callback https://dearpygui.readthedocs.io/en/latest/documentation/item-callbacks.html

import dearpygui.dearpygui as dpg

dpg.create_context()

def button_callback(sender, app_data, user_data):
    # with dpg.window(label=f"{sender}"):       
    #     dpg.add_text(f"sender: {sender} \napp_data: {app_data} \nuser_data: {user_data}") 
    
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")


with dpg.window(label="Callbacks"):
        # user_data and callback is set when button is created
        dpg.add_button(label="Apply", callback=button_callback, user_data="Some Data")

        # user_data and callback set any time after button has been created
        btn = dpg.add_button(label="Apply 2")
        dpg.set_item_callback(btn, button_callback)
        dpg.set_item_user_data(btn, "Some Extra User Data")


dpg.create_viewport(title="Callbacks", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()