# o with gerencia recursos, ele é expecialmente util quando temos muitos recursos acontecendo e precisamos inicialos
# e desativalos apos o uso, ele fas esse "__init__" , "__exit__" de forma automatica, facilitando o gerenciamento.
# Mesmo que o codigo apresente uma excessão ele continua o fechamento dos recursos que foram abertos. 
# para o davi do futuro, mergulhe novamente, mais fudo desta vez ...
# ... em: https://www.geeksforgeeks.org/with-statement-in-python/

# Good links for deep swin in Handlers:
    # https://dearpygui.readthedocs.io/en/latest/documentation/io-handlers-state.html
    # https://dearpygui.readthedocs.io/en/latest/documentation/container-slots.html
    # https://dearpygui.readthedocs.io/en/latest/documentation/container-stack.html]

import dearpygui.dearpygui as dpg

dpg.create_context()

def change_text(sender, app_data, user_data):
    dpg.set_value("text item", f"Mouse Button ID: {app_data}")
    # print(f"sender: {sender}\n", f"app data: {app_data}\n", f"user_data: {user_data}\n") 


with dpg.window(width=500, height=300):
    dpg.add_text("Click me with any mouse button", tag="text item")
    
    # this as handler is trash code, because in this situations i not use them, but is coll now we can use this notation
    # with them
    with dpg.item_handler_registry(tag="widget handler") as handler: 
        dpg.add_item_clicked_handler(callback=change_text)
        # este item-> add_item_clicked_handler tem um app_data que é naturalmente retornado por sua built-in function:
        # (int|str). 
        # Os dados deste item, como 'sender'(id), 'user_data'(qual quer obj python atribuido a ele) e
        # 'app_data'(que são os dados que ele ira capturar do click/ neste objeto são os clicks dos botões do mause)
    
    dpg.bind_item_handler_registry("text item", "widget handler")

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()